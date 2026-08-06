#!/usr/bin/env python3
"""
Phase 1: SNI Direct Read Test for SMRPG (SA-1)

Tests whether FXPak Pro + SNI can directly read various memory regions
without requiring cooperative ROM patches. This determines whether
Phase 2 (NMI hook) is needed.

Tests three memory regions:
  1. WRAM ($7E/$7F) - via FxPakPro address space (should always work)
  2. BW-RAM ($00:7040+) - via SnesABus (SA-1 dependent)
  3. IRAM ($00:3030+) - via SnesABus (SA-1 internal, may fail)

Also tests alternate BW-RAM access via $40 bank mirror.

Usage:
    # Activate venv first:
    source tools/.venv/bin/activate
    python tools/sni_test.py [--host HOST:PORT] [--verbose]

Requirements:
    pip install snirk
    SNI must be running and FXPak Pro connected with SMRPG loaded.
"""

import argparse
import asyncio
import sys
import traceback

import grpc
from snirk import Snirk
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni

from smrpg_memmap import (
    WRAMAddresses,
    BWRAMAddresses,
    BWRAMMirrorAddresses,
    IRAMAddresses,
    AREA_NAMES,
    CHARACTER_NAMES,
    EVENT_FLAGS,
    parse_character_stats,
    parse_event_flags,
)


def hex_dump(data: bytes, start_addr: int = 0, width: int = 16) -> str:
    """Format bytes as a hex dump."""
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        lines.append(f"  ${start_addr + i:06X}: {hex_part:<{width * 3}}  {ascii_part}")
    return "\n".join(lines)


async def read_fxpakpro(
    channel_str: str, device_uri: str, address: int, size: int
) -> bytes | None:
    """Read using FxPakPro address space (default snirk behavior)."""
    try:
        with grpc.insecure_channel(channel_str) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.ReadMemoryRequest(
                requestAddress=address,
                requestAddressSpace=pb.AddressSpace.FxPakPro,
                size=size,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=device_uri, request=request)
            )
            return bytes(response.response.data)
    except Exception as e:
        return None


async def read_snes_abus(
    channel_str: str, device_uri: str, address: int, size: int,
    mapping: pb.MemoryMapping = pb.MemoryMapping.SA1,
) -> bytes | None:
    """Read using SNES A-Bus address space with SA-1 memory mapping."""
    try:
        with grpc.insecure_channel(channel_str) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.ReadMemoryRequest(
                requestAddress=address,
                requestAddressSpace=pb.AddressSpace.SnesABus,
                requestMemoryMapping=mapping,
                size=size,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=device_uri, request=request)
            )
            return bytes(response.response.data)
    except Exception as e:
        return None


async def read_raw(
    channel_str: str, device_uri: str, address: int, size: int,
) -> bytes | None:
    """Read using Raw address space (pass-through to device)."""
    try:
        with grpc.insecure_channel(channel_str) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.ReadMemoryRequest(
                requestAddress=address,
                requestAddressSpace=pb.AddressSpace.Raw,
                size=size,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=device_uri, request=request)
            )
            return bytes(response.response.data)
    except Exception as e:
        return None


def is_all_zeros(data: bytes) -> bool:
    return all(b == 0 for b in data)


def is_all_ff(data: bytes) -> bool:
    return all(b == 0xFF for b in data)


def data_looks_valid(data: bytes) -> str:
    """Quick heuristic check on whether data looks like real game state."""
    if is_all_zeros(data):
        return "ALL ZEROS (possibly uninitialized or unmapped)"
    if is_all_ff(data):
        return "ALL 0xFF (possibly unmapped/bus noise)"
    unique = len(set(data))
    if unique == 1:
        return f"ALL 0x{data[0]:02X} (suspicious)"
    return f"OK ({unique} unique values in {len(data)} bytes)"


async def test_connection(snirk_client: Snirk, verbose: bool) -> tuple[str, str]:
    """Test SNI connection and return device info."""
    print("=" * 60)
    print("SNI Connection Test")
    print("=" * 60)

    try:
        devices = await snirk_client.list_devices(timeout=5)
    except Exception as e:
        print(f"FAIL: Cannot connect to SNI at {snirk_client.channel}")
        print(f"  Error: {e}")
        print(f"  Make sure SNI is running!")
        sys.exit(1)

    if not devices:
        print("FAIL: No devices found. Connect FXPak Pro and load a ROM.")
        sys.exit(1)

    for dev in devices:
        kind = dev.kind
        uri = dev.uri
        name = dev.displayName
        caps = [c for c in dev.capabilities]
        print(f"  Device: {name}")
        print(f"  Kind:   {kind}")
        print(f"  URI:    {uri}")
        print(f"  Caps:   {len(caps)} capabilities")
        if verbose:
            cap_names = {
                pb.DeviceCapability.ReadMemory: "ReadMemory",
                pb.DeviceCapability.WriteMemory: "WriteMemory",
                pb.DeviceCapability.ExecuteASM: "ExecuteASM",
                pb.DeviceCapability.ResetSystem: "ResetSystem",
                pb.DeviceCapability.FetchFields: "FetchFields",
                pb.DeviceCapability.ReadDirectory: "ReadDirectory",
                pb.DeviceCapability.PutFile: "PutFile",
                pb.DeviceCapability.GetFile: "GetFile",
                pb.DeviceCapability.BootFile: "BootFile",
            }
            for cap in caps:
                print(f"    - {cap_names.get(cap, f'Unknown({cap})')}")

    device = devices[0]

    try:
        with grpc.insecure_channel(snirk_client.channel) as ch:
            stub = sni.DeviceMemoryStub(ch)
            mm_response = stub.MappingDetect(
                pb.DetectMemoryMappingRequest(uri=device.uri)
            )
            mapping = mm_response.memoryMapping
            mapping_names = {
                pb.MemoryMapping.Unknown: "Unknown",
                pb.MemoryMapping.HiROM: "HiROM",
                pb.MemoryMapping.LoROM: "LoROM",
                pb.MemoryMapping.ExHiROM: "ExHiROM",
                pb.MemoryMapping.SA1: "SA1",
            }
            print(f"  Memory Mapping: {mapping_names.get(mapping, '???')}")
            if mapping != pb.MemoryMapping.SA1:
                print("  WARNING: Expected SA1 mapping for SMRPG!")
    except Exception as e:
        print(f"  Memory mapping detection failed: {e}")

    print()
    return device.uri, snirk_client.channel


async def test_wram(channel: str, uri: str, verbose: bool) -> dict:
    """Test WRAM reads via FxPakPro address space."""
    print("=" * 60)
    print("Test 1: WRAM via FxPakPro Address Space")
    print("  (SNES $7E/$7F -> FxPakPro $F5/$F6)")
    print("=" * 60)
    results = {}

    print("\n  Reading character stats ($7F:F800, 0xB9 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF6F800, 0xB9)
    if data is None:
        print("  FAIL: Read returned None (gRPC error)")
        results["character_stats"] = False
    else:
        validity = data_looks_valid(data)
        results["character_stats"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0x7FF800))
        if results["character_stats"]:
            for i in range(5):
                try:
                    stats = parse_character_stats(data, i)
                    lv = stats['level']
                    hp = stats['current_hp']
                    maxhp = stats['max_hp']
                    atk = stats['attack']
                    if lv > 0 and lv <= 30 and maxhp > 0 and maxhp <= 999:
                        print(f"    {stats['name']}: Lv{lv} HP {hp}/{maxhp} "
                              f"Atk:{atk} Def:{stats['defense']} "
                              f"MgA:{stats['mg_attack']} MgD:{stats['mg_defense']}")
                    elif lv == 0 and maxhp == 0:
                        print(f"    {stats['name']}: (not in party / uninitialized)")
                    else:
                        print(f"    {stats['name']}: Lv{lv} HP {hp}/{maxhp} "
                              f"(values look suspicious)")
                except Exception as e:
                    print(f"    {CHARACTER_NAMES.get(i, '?')}: Parse error: {e}")

    print("\n  Reading coins ($7F:F8B9, 2 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF6F8B9, 2)
    if data is not None:
        coins = int.from_bytes(data, "little")
        print(f"  Coins: {coins}")
        results["coins"] = coins <= 999
    else:
        print("  FAIL: Read returned None")
        results["coins"] = False

    print("\n  Reading frog coins ($7F:F8BB, 2 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF6F8BB, 2)
    if data is not None:
        frog_coins = int.from_bytes(data, "little")
        print(f"  Frog Coins: {frog_coins}")
        results["frog_coins"] = frog_coins <= 999
    else:
        print("  FAIL: Read returned None")
        results["frog_coins"] = False

    print("\n  Reading battle formation ($7E:0048, 2 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF50048, 2)
    if data is not None:
        formation = int.from_bytes(data, "little")
        print(f"  Formation: {formation}")
        results["battle_formation"] = True
    else:
        print("  FAIL: Read returned None")
        results["battle_formation"] = False

    print("\n  Reading map location ($7E:09E5, 2 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF509E5, 2)
    if data is not None:
        location = int.from_bytes(data, "little")
        print(f"  Map Location: {location}")
        results["map_location"] = True
    else:
        print("  FAIL: Read returned None")
        results["map_location"] = False

    print()
    return results


async def test_bwram_snes_abus(channel: str, uri: str, verbose: bool) -> dict:
    """Test BW-RAM reads via SNES A-Bus with SA-1 mapping."""
    print("=" * 60)
    print("Test 2: BW-RAM via SNES A-Bus (SA-1 mapping)")
    print("  ($00:7040+ event flags, SA-1 BW-RAM)")
    print("=" * 60)
    results = {}

    print("\n  Reading event flags ($00:7040, 96 bytes)...")
    data = await read_snes_abus(channel, uri, 0x007040, 0x60)
    if data is None:
        print("  FAIL: Read returned None (address space not supported?)")
        results["event_flags_abus"] = False
    else:
        validity = data_looks_valid(data)
        results["event_flags_abus"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0x7040))
        if results["event_flags_abus"]:
            flags = parse_event_flags(data)
            set_flags = [name for name, val in flags.items() if val]
            if set_flags:
                print(f"  Active flags ({len(set_flags)}):")
                for flag in set_flags[:15]:
                    print(f"    - {flag}")
                if len(set_flags) > 15:
                    print(f"    ... and {len(set_flags) - 15} more")
            else:
                print("  No progression flags set (early game or flags at $00 somehow)")

    print("\n  Reading menu flags ($00:7062, 1 byte)...")
    data = await read_snes_abus(channel, uri, 0x007062, 1)
    if data is not None:
        val = data[0]
        print(f"  Raw: 0x{val:02X}")
        if val & 0x01: print("    - Map Menu Unlocked")
        if val & 0x02: print("    - Star Piece Menu Unlocked")
        if val & 0x04: print("    - Switch Menu Unlocked")
        if val & 0x08: print("    - Beetlemania Unlocked")
        results["menu_flags_abus"] = True
    else:
        print("  FAIL: Read returned None")
        results["menu_flags_abus"] = False

    print("\n  Reading hidden chest counter ($00:70C8, 1 byte)...")
    data = await read_snes_abus(channel, uri, 0x0070C8, 1)
    if data is not None:
        print(f"  Hidden chests found: {data[0]}")
        results["hidden_chests_abus"] = True
    else:
        print("  FAIL: Read returned None")
        results["hidden_chests_abus"] = False

    print()
    return results


async def test_bwram_mirror(channel: str, uri: str, verbose: bool) -> dict:
    """Test BW-RAM reads via $40 bank mirror."""
    print("=" * 60)
    print("Test 3: BW-RAM via $40 Bank Mirror (SNES A-Bus)")
    print("  ($40:7040+ alternate BW-RAM access)")
    print("=" * 60)
    results = {}

    print("\n  Reading event flags ($40:7040, 96 bytes)...")
    data = await read_snes_abus(channel, uri, 0x407040, 0x60)
    if data is None:
        print("  FAIL: Read returned None")
        results["event_flags_mirror"] = False
    else:
        validity = data_looks_valid(data)
        results["event_flags_mirror"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0x407040))
        if results["event_flags_mirror"]:
            flags = parse_event_flags(data)
            set_flags = [name for name, val in flags.items() if val]
            print(f"  Active flags: {len(set_flags)}")

    print()
    return results


async def test_iram(channel: str, uri: str, verbose: bool) -> dict:
    """Test SA-1 IRAM reads."""
    print("=" * 60)
    print("Test 4: SA-1 IRAM via SNES A-Bus")
    print("  ($00:3030+ current area, party data)")
    print("=" * 60)
    results = {}

    print("\n  Reading current area ($00:3030, 2 bytes)...")
    data = await read_snes_abus(channel, uri, 0x003030, 2)
    if data is None:
        print("  FAIL: Read returned None")
        results["current_area_iram"] = False
    else:
        area_id = int.from_bytes(data, "little")
        area_name = AREA_NAMES.get(area_id, f"Unknown ({area_id})")
        print(f"  Area ID: {area_id} = {area_name}")
        results["current_area_iram"] = area_id < 256  # sanity check
        if verbose:
            print(hex_dump(data, 0x3030))

    print("\n  Reading party slots ($00:3032, 14 bytes)...")
    data = await read_snes_abus(channel, uri, 0x003032, 0x0E)
    if data is None:
        print("  FAIL: Read returned None")
        results["party_slots_iram"] = False
    else:
        validity = data_looks_valid(data)
        results["party_slots_iram"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0x3032))
        if results["party_slots_iram"]:
            for i in range(min(5, len(data))):
                char_id = data[i]
                name = CHARACTER_NAMES.get(char_id, f"Unknown({char_id})")
                print(f"    Slot {i}: {name} (0x{char_id:02X})")

    print("\n  Reading party count ($00:303F, 1 byte)...")
    data = await read_snes_abus(channel, uri, 0x00303F, 1)
    if data is not None:
        count = data[0]
        print(f"  Party members: {count}")
        results["party_count_iram"] = count <= 5
    else:
        print("  FAIL: Read returned None")
        results["party_count_iram"] = False

    # Also try via $40 mirror
    print("\n  Reading current area via $40 mirror ($40:3030, 2 bytes)...")
    data = await read_snes_abus(channel, uri, 0x403030, 2)
    if data is not None:
        area_id = int.from_bytes(data, "little")
        area_name = AREA_NAMES.get(area_id, f"Unknown ({area_id})")
        print(f"  Area ID: {area_id} = {area_name}")
        results["current_area_mirror"] = area_id < 256
    else:
        print("  FAIL: Read returned None")
        results["current_area_mirror"] = False

    print()
    return results


async def test_sram_space(channel: str, uri: str, verbose: bool) -> dict:
    """Test BW-RAM reads via FxPakPro SRAM address space ($E00000+).

    For SA-1 games, BW-RAM is battery-backed and should map into the
    FxPakPro SRAM region. This is the most likely way to access event
    flags on real hardware.
    """
    print("=" * 60)
    print("Test 5: BW-RAM via FxPakPro SRAM Space ($E00000+)")
    print("  SA-1 BW-RAM is the SRAM - try multiple offsets")
    print("=" * 60)
    results = {}

    # BW-RAM in SMRPG: event flags are at $00:7040 in SA-1 address space.
    # BW-RAM base is $00:6000 in SA-1 space, so offset within BW-RAM = $1040.
    # But we don't know the exact FxPakPro SRAM mapping, so try several.
    #
    # Possibilities:
    #   $E00000 + $7040 = $E07040  (BW-RAM mapped at SRAM base + SA-1 addr)
    #   $E00000 + $1040 = $E01040  (BW-RAM offset: $7040 - $6000 base)
    #   $E00000 + $0000 = $E00000  (just dump SRAM start to see what's there)

    test_addrs = [
        (0xE00000, 0x100, "SRAM base $E00000 (first 256 bytes)"),
        (0xE01040, 0x60,  "SRAM $E01040 (BW-RAM offset $1040 = $7040-$6000)"),
        (0xE07040, 0x60,  "SRAM $E07040 (SA-1 addr $7040 direct)"),
        (0xE06000, 0x80,  "SRAM $E06000 (BW-RAM base $6000)"),
        (0xE00000, 0x60,  "SRAM $E00000 (BW-RAM at offset 0)"),
        (0xE10000, 0x60,  "SRAM $E10000 (second 64KB bank)"),
        (0xE17040, 0x60,  "SRAM $E17040 (second bank + $7040)"),
    ]

    found_valid = False
    for addr, size, desc in test_addrs:
        print(f"\n  Reading {desc}...")
        data = await read_fxpakpro(channel, uri, addr, size)
        if data is None:
            print(f"  FAIL: Read returned None")
            continue

        validity = data_looks_valid(data)
        print(f"  Result: {validity}")

        if verbose or "OK" in validity:
            print(hex_dump(data, addr))

        if "OK" in validity:
            # Check if this looks like event flags (some bits set, not all 0 or FF)
            nonzero = sum(1 for b in data if b != 0)
            print(f"  Non-zero bytes: {nonzero}/{len(data)}")

            # If reading 96 bytes, try to parse as event flags
            if size == 0x60:
                flags = parse_event_flags(data)
                set_flags = [name for name, val in flags.items() if val]
                if set_flags:
                    print(f"  Parsed as event flags ({len(set_flags)} set):")
                    for flag in set_flags[:10]:
                        print(f"    - {flag}")
                    if len(set_flags) > 10:
                        print(f"    ... and {len(set_flags) - 10} more")
                    results[f"sram_{addr:06X}"] = True
                    found_valid = True
                else:
                    print(f"  Parsed as event flags: 0 set (may not be flags)")

    results["sram_any_valid"] = found_valid

    # Also try larger SRAM dump to find where BW-RAM data lives
    print(f"\n  Scanning SRAM for non-trivial data (first 128KB)...")
    scan_hits = []
    for offset in range(0, 0x20000, 0x1000):
        addr = 0xE00000 + offset
        data = await read_fxpakpro(channel, uri, addr, 0x40)
        if data is not None:
            unique = len(set(data))
            nonzero = sum(1 for b in data if b != 0)
            if unique > 3 and nonzero > 2:
                scan_hits.append((addr, offset, unique, nonzero))

    if scan_hits:
        print(f"  Found {len(scan_hits)} regions with varied data:")
        for addr, offset, unique, nonzero in scan_hits[:20]:
            print(f"    ${addr:06X} (offset ${offset:05X}): "
                  f"{unique} unique, {nonzero}/64 nonzero")
            if verbose:
                data = await read_fxpakpro(channel, uri, addr, 0x40)
                if data is not None:
                    print(hex_dump(data, addr))
    else:
        print("  No varied data found in SRAM region!")

    print()
    return results


async def test_raw_reads(channel: str, uri: str, verbose: bool) -> dict:
    """Test reads via Raw address space (direct device pass-through)."""
    print("=" * 60)
    print("Test 6: Raw Address Space (device pass-through)")
    print("=" * 60)
    results = {}

    print("\n  Reading WRAM via Raw ($F6F800, 0x25 bytes)...")
    data = await read_raw(channel, uri, 0xF6F800, 0x25)
    if data is not None:
        validity = data_looks_valid(data)
        results["wram_raw"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0xF6F800))
    else:
        print("  FAIL: Read returned None")
        results["wram_raw"] = False

    # Try BW-RAM via Raw (note: in FxPakPro raw space, $007040 = ROM!)
    print("\n  Reading Raw $007040 (this is ROM, not BW-RAM!)...")
    data = await read_raw(channel, uri, 0x007040, 0x60)
    if data is not None:
        validity = data_looks_valid(data)
        results["bwram_raw"] = "OK" in validity
        print(f"  Result: {validity}")
        if verbose:
            print(hex_dump(data, 0x007040))
    else:
        print("  FAIL: Read returned None")
        results["bwram_raw"] = False

    print("\n  Reading WRAM $7E:0000 via FxPakPro ($F50000, 64 bytes)...")
    data = await read_fxpakpro(channel, uri, 0xF50000, 0x40)
    if data is not None:
        validity = data_looks_valid(data)
        print(f"  Result: {validity}")
        results["wram_low"] = "OK" in validity
        if verbose:
            print(hex_dump(data, 0xF50000))
    else:
        print("  FAIL: Read returned None")
        results["wram_low"] = False

    print()
    return results


async def coherency_test(channel: str, uri: str, verbose: bool) -> dict:
    """Read the same addresses twice quickly to check for coherency."""
    print("=" * 60)
    print("Test 7: Coherency Check (read twice, compare)")
    print("=" * 60)
    results = {}

    # Read WRAM character block twice
    print("\n  Reading character block twice...")
    data1 = await read_fxpakpro(channel, uri, 0xF6F800, 0xB9)
    data2 = await read_fxpakpro(channel, uri, 0xF6F800, 0xB9)
    if data1 is not None and data2 is not None:
        match = data1 == data2
        print(f"  Match: {match}")
        if not match:
            diffs = sum(1 for a, b in zip(data1, data2) if a != b)
            print(f"  Differences: {diffs} bytes")
            if verbose:
                for i, (a, b) in enumerate(zip(data1, data2)):
                    if a != b:
                        print(f"    Offset 0x{i:03X}: 0x{a:02X} -> 0x{b:02X}")
        results["wram_coherent"] = match
    else:
        print("  FAIL: One or both reads returned None")
        results["wram_coherent"] = False

    # Read event flags twice if SNES A-Bus works
    print("\n  Reading event flags twice via SnesABus...")
    data1 = await read_snes_abus(channel, uri, 0x007040, 0x60)
    data2 = await read_snes_abus(channel, uri, 0x007040, 0x60)
    if data1 is not None and data2 is not None:
        match = data1 == data2
        print(f"  Match: {match}")
        results["bwram_coherent"] = match
    else:
        print("  FAIL: SnesABus reads not available for coherency check")
        results["bwram_coherent"] = None

    print()
    return results


async def main():
    parser = argparse.ArgumentParser(
        description="SNI Direct Read Test for SMRPG (SA-1)"
    )
    parser.add_argument(
        "--host", default="localhost:8191",
        help="SNI host:port (default: localhost:8191)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show hex dumps of read data"
    )
    args = parser.parse_args()

    snirk_client = Snirk(channel=args.host)

    uri, channel = await test_connection(snirk_client, args.verbose)

    all_results = {}
    all_results.update(await test_wram(channel, uri, args.verbose))
    all_results.update(await test_bwram_snes_abus(channel, uri, args.verbose))
    all_results.update(await test_bwram_mirror(channel, uri, args.verbose))
    all_results.update(await test_iram(channel, uri, args.verbose))
    all_results.update(await test_sram_space(channel, uri, args.verbose))
    all_results.update(await test_raw_reads(channel, uri, args.verbose))
    all_results.update(await coherency_test(channel, uri, args.verbose))

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print()

    wram_ok = all(
        v for k, v in all_results.items()
        if k in ("character_stats", "coins", "frog_coins", "battle_formation", "map_location")
    )
    bwram_abus_ok = all(
        v for k, v in all_results.items()
        if k.endswith("_abus")
    )
    bwram_mirror_ok = all(
        v for k, v in all_results.items()
        if k.endswith("_mirror") and k.startswith("event")
    )
    iram_ok = all(
        v for k, v in all_results.items()
        if k.endswith("_iram")
    )
    area_mirror_ok = all_results.get("current_area_mirror", False)
    sram_ok = all_results.get("sram_any_valid", False)

    print(f"  WRAM (FxPakPro):           {'PASS' if wram_ok else 'FAIL'}")
    print(f"  BW-RAM (SnesABus $00:):    {'PASS' if bwram_abus_ok else 'FAIL'}")
    print(f"  BW-RAM ($40 mirror):       {'PASS' if bwram_mirror_ok else 'FAIL'}")
    print(f"  BW-RAM (SRAM $E0xxxx):     {'PASS' if sram_ok else 'FAIL'}")
    print(f"  IRAM (SnesABus $00:30xx):  {'PASS' if iram_ok else 'FAIL'}")
    print(f"  IRAM ($40 mirror):         {'PASS' if area_mirror_ok else 'FAIL'}")
    print()

    coherent = all_results.get("wram_coherent", False)
    bwram_coherent = all_results.get("bwram_coherent")
    print(f"  WRAM coherency:            {'PASS' if coherent else 'FAIL'}")
    if bwram_coherent is not None:
        print(f"  BW-RAM coherency:          {'PASS' if bwram_coherent else 'FAIL'}")
    else:
        print(f"  BW-RAM coherency:          N/A (reads failed)")

    print()
    print("Recommendation:")
    if wram_ok and bwram_abus_ok and iram_ok:
        print("  ALL reads work! Phase 2 (NMI hook) is NOT needed.")
        print("  Proceed directly to Phase 3 (monitor/autotracker).")
    elif wram_ok and (bwram_abus_ok or bwram_mirror_ok):
        if iram_ok or area_mirror_ok:
            print("  WRAM + BW-RAM + IRAM all accessible (possibly via mirrors).")
            print("  Phase 2 (NMI hook) is NOT needed.")
        else:
            print("  WRAM and BW-RAM work, but IRAM ($3030+) does not.")
            print("  Phase 2 needed ONLY for: current area, party composition.")
            print("  These are relatively small - a minimal NMI hook suffices.")
    elif wram_ok:
        print("  Only WRAM reads work. BW-RAM and IRAM are not accessible.")
        print("  Phase 2 (NMI hook) IS needed to copy event flags + party data.")
    else:
        print("  WRAM reads also failing - check connection and game state.")

    print()
    # Print which address space to use for each region
    print("Address space to use for each region:")
    print(f"  Character stats:  FxPakPro $F6F800  {'OK' if all_results.get('character_stats') else 'FAIL'}")
    print(f"  Coins:            FxPakPro $F6F8B9  {'OK' if all_results.get('coins') else 'FAIL'}")
    if bwram_abus_ok:
        print(f"  Event flags:      SnesABus $007040  OK")
    elif bwram_mirror_ok:
        print(f"  Event flags:      SnesABus $407040  OK (via mirror)")
    else:
        print(f"  Event flags:      UNAVAILABLE - needs NMI hook")
    if iram_ok:
        print(f"  Current area:     SnesABus $003030  OK")
    elif area_mirror_ok:
        print(f"  Current area:     SnesABus $403030  OK (via mirror)")
    else:
        print(f"  Current area:     UNAVAILABLE - needs NMI hook")


if __name__ == "__main__":
    asyncio.run(main())
