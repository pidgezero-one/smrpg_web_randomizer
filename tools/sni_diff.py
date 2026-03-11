#!/usr/bin/env python3
"""
SRAM Differential Test - Find where live game state lives in FxPakPro SRAM.

Takes two snapshots of the SRAM region, with the user making an in-game
change between them, then reports which bytes changed.

Usage:
    python tools/sni_diff.py --host 172.26.240.1:8191

    1. Script reads SRAM snapshot A
    2. Prompts you to do something in-game (collect coins, move rooms, etc.)
    3. Script reads SRAM snapshot B
    4. Shows all bytes that changed, grouped by region
"""

import argparse
import asyncio
import sys
from pathlib import Path

import grpc
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni


def read_fxpakpro(channel_str: str, device_uri: str, address: int, size: int) -> bytes | None:
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
        print(f"  Read error at ${address:06X}: {e}")
        return None


def find_device(channel_str: str) -> str | None:
    try:
        with grpc.insecure_channel(channel_str) as ch:
            stub = sni.DevicesStub(ch)
            response = stub.ListDevices(pb.DevicesRequest(kinds=[]))
            if response and response.devices:
                return response.devices[0].uri
    except Exception as e:
        print(f"Connection error: {e}")
    return None


def read_full_sram(channel_str: str, uri: str, size: int = 0x20000) -> bytes | None:
    """Read the full SRAM region in chunks."""
    chunk_size = 0x800  # 2KB chunks to avoid timeouts
    data = bytearray()

    for offset in range(0, size, chunk_size):
        addr = 0xE00000 + offset
        remaining = min(chunk_size, size - offset)
        chunk = read_fxpakpro(channel_str, uri, addr, remaining)
        if chunk is None:
            print(f"  Failed at offset ${offset:05X}, padding with 0xFF")
            data.extend(b'\xFF' * remaining)
        else:
            data.extend(chunk)

        # Progress indicator
        pct = (offset + remaining) * 100 // size
        print(f"\r  Reading SRAM... {pct}%", end="", flush=True)

    print()
    return bytes(data)


def hex_dump_line(data: bytes, addr: int) -> str:
    hex_part = " ".join(f"{b:02X}" for b in data)
    ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in data)
    return f"${addr:06X}: {hex_part}  {ascii_part}"


def compare_snapshots(snap_a: bytes, snap_b: bytes, base_addr: int = 0xE00000) -> list[tuple[int, int, int]]:
    """Compare two snapshots and return list of (offset, old_val, new_val)."""
    diffs = []
    for i in range(min(len(snap_a), len(snap_b))):
        if snap_a[i] != snap_b[i]:
            diffs.append((i, snap_a[i], snap_b[i]))
    return diffs


def group_diffs(diffs: list[tuple[int, int, int]], gap: int = 16) -> list[list[tuple[int, int, int]]]:
    """Group nearby diffs together."""
    if not diffs:
        return []

    groups: list[list[tuple[int, int, int]]] = [[diffs[0]]]
    for diff in diffs[1:]:
        if diff[0] - groups[-1][-1][0] <= gap:
            groups[-1].append(diff)
        else:
            groups.append([diff])
    return groups


async def main():
    parser = argparse.ArgumentParser(description="SRAM Differential Test")
    parser.add_argument("--host", default="localhost:8191", help="SNI host:port")
    parser.add_argument("--size", type=lambda x: int(x, 0), default=0x20000,
                        help="SRAM size to read in hex (default: 0x20000 = 128KB)")
    parser.add_argument("--output", "-o", default="tools/sni_diff_output.txt",
                        help="Output file (default: tools/sni_diff_output.txt)")
    args = parser.parse_args()

    output_path = Path(args.output)
    outfile = open(output_path, "w")

    def out(msg: str = "") -> None:
        print(msg)
        outfile.write(msg + "\n")

    out("SRAM Differential Test")
    out("=" * 60)

    uri = find_device(args.host)
    if not uri:
        out("Failed to connect. Is SNI running?")
        sys.exit(1)
    out(f"Connected: {uri}")

    # Snapshot A
    print(f"\nSnapshot A: Reading {args.size // 1024}KB of SRAM...")
    snap_a = read_full_sram(args.host, uri, args.size)
    if snap_a is None:
        out("Failed to read SRAM")
        sys.exit(1)
    out(f"\nSnapshot A: {args.size // 1024}KB read OK")

    # Wait for user action
    print("\n" + "=" * 60)
    print("NOW: Do something in-game that changes state.")
    print("Suggestions:")
    print("  - Collect some coins (changes coin counter)")
    print("  - Walk to a different room/area (changes current area)")
    print("  - Open a chest (changes event flags)")
    print("  - Save the game (changes save data region)")
    print("  - Trigger an event/cutscene")
    print()
    input("Press Enter when done... ")
    print()

    # Snapshot B
    print(f"Snapshot B: Reading {args.size // 1024}KB of SRAM...")
    snap_b = read_full_sram(args.host, uri, args.size)
    if snap_b is None:
        out("Failed to read SRAM")
        sys.exit(1)
    out(f"Snapshot B: {args.size // 1024}KB read OK")

    # Compare
    diffs = compare_snapshots(snap_a, snap_b)
    out(f"\n{'=' * 60}")
    out(f"RESULTS: {len(diffs)} bytes changed")
    out(f"{'=' * 60}")

    if not diffs:
        out("\nNo changes detected!")
        out("Either:")
        out("  - The action didn't change SRAM-visible state")
        out("  - BW-RAM is not readable through SRAM space while game runs")
        out("  - Try saving the game, then take snapshot B")
        outfile.close()
        print(f"\nOutput written to {output_path}")
        return

    # Group and display
    groups = group_diffs(diffs)
    out(f"\nChanges in {len(groups)} region(s):\n")

    for group in groups:
        start_offset = group[0][0]
        end_offset = group[-1][0]
        sram_addr = 0xE00000 + start_offset

        # Map to SNES BW-RAM address: SRAM offset - $2000 + $6000 = SRAM offset + $4000
        bwram_addr = start_offset + 0x4000
        bwram_end = end_offset + 0x4000

        out(f"  Region: SRAM ${sram_addr:06X}-${0xE00000 + end_offset:06X} "
            f"(offset ${start_offset:05X}-${end_offset:05X}, "
            f"BW-RAM ${bwram_addr:04X}-${bwram_end:04X}, "
            f"{len(group)} bytes changed)")

        # Show context: 16 bytes around each change
        shown_ranges: set[int] = set()
        for offset, old_val, new_val in group:
            # Align to 16-byte boundary for context
            line_start = (offset // 16) * 16
            if line_start in shown_ranges:
                continue
            shown_ranges.add(line_start)

            line_end = min(line_start + 16, len(snap_a))
            line_a = snap_a[line_start:line_end]
            line_b = snap_b[line_start:line_end]

            addr = 0xE00000 + line_start
            out(f"    A: {hex_dump_line(line_a, addr)}")
            out(f"    B: {hex_dump_line(line_b, addr)}")

            # Highlight specific changes
            for off, old, new in group:
                if line_start <= off < line_end:
                    col = off - line_start
                    bw = off + 0x4000
                    out(f"       {'   ' * col}^^ ${off:05X} (BW-RAM ${bw:04X}): "
                        f"0x{old:02X} -> 0x{new:02X}")
            out()

    # Summary: which 4KB blocks had changes?
    out("Changed 4KB blocks:")
    changed_blocks: dict[int, int] = {}
    for offset, _, _ in diffs:
        block = (offset // 0x1000) * 0x1000
        changed_blocks[block] = changed_blocks.get(block, 0) + 1

    for block, count in sorted(changed_blocks.items()):
        addr = 0xE00000 + block
        out(f"  ${addr:06X}-${addr + 0xFFF:06X}: {count} byte(s) changed")

    outfile.close()
    print(f"\nOutput written to {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
