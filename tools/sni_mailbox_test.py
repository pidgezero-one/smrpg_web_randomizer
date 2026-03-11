#!/usr/bin/env python3
"""Test the NMI cooperative hook's BW-RAM mailbox via FxPakPro.

Reads the mailbox region to verify the hook is running, then optionally
sends test commands (state dump, give item, etc.) and checks responses.

Usage:
    python tools/sni_mailbox_test.py --host 172.26.240.1:8191
"""

import argparse
import sys
import time

import grpc
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni

# Import mailbox constants
sys.path.insert(0, ".")
from randomizer.data.nmi_hook import (
    MAILBOX_FXPAK_BASE,
    OUTBOX_MUSIC,
    OUTBOX_BATTLE,
    OUTBOX_FRAME_CTR,
    OUTBOX_VERSION,
    OUTBOX_RESULT,
    OUTBOX_GAME_MODE,
    OUTBOX_CONSUMABLES,
    OUTBOX_EQUIPMENT,
    OUTBOX_KEY_ITEMS,
    OUTBOX_COINS,
    OUTBOX_FROG_COINS,
    OUTBOX_CURRENT_FP,
    OUTBOX_MAX_FP,
    OUTBOX_CUR_HP,
    OUTBOX_MAX_HP,
    INBOX_COMMAND,
    CMD_GIVE_ITEM,
    CMD_SET_COINS,
    CMD_SET_FROG_COINS,
    CMD_ADD_COINS,
    CMD_ADD_FROG_COINS,
    CMD_ADD_STAR_PIECE,
    CMD_RECRUIT_CHAR,
    CMD_LEARN_SPELL,
    CMD_STATE_DUMP,
    CMD_HEAL,
    HOOK_VERSION,
    RESULT_OK,
    RESULT_INV_FULL,
)


def find_device(host: str) -> str | None:
    try:
        with grpc.insecure_channel(host) as ch:
            stub = sni.DevicesStub(ch)
            response = stub.ListDevices(pb.DevicesRequest(kinds=[]))
            if response and response.devices:
                return response.devices[0].uri
    except Exception as e:
        print(f"Connection error: {e}")
    return None


def read_mailbox(host: str, uri: str, offset: int = 0, size: int = 0x100, retries: int = 3) -> bytes | None:
    """Read from the mailbox region in FxPakPro SRAM space."""
    addr = MAILBOX_FXPAK_BASE + offset
    for attempt in range(retries):
        try:
            with grpc.insecure_channel(host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.ReadMemoryRequest(
                    requestAddress=addr,
                    requestAddressSpace=pb.AddressSpace.FxPakPro,
                    size=size,
                )
                response = stub.SingleRead(
                    pb.SingleReadMemoryRequest(uri=uri, request=request)
                )
                return bytes(response.response.data)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(0.5)
            else:
                print(f"  Read error at ${addr:06X}: {e}")
    return None


def write_mailbox(host: str, uri: str, offset: int, data: bytes) -> bool:
    """Write to the mailbox region in FxPakPro SRAM space."""
    addr = MAILBOX_FXPAK_BASE + offset
    try:
        with grpc.insecure_channel(host) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.WriteMemoryRequest(
                requestAddress=addr,
                requestAddressSpace=pb.AddressSpace.FxPakPro,
                data=data,
            )
            stub.SingleWrite(
                pb.SingleWriteMemoryRequest(uri=uri, request=request)
            )
            return True
    except Exception as e:
        print(f"  Write error at ${addr:06X}: {e}")
        return False


def read_fxpak(host: str, uri: str, addr: int, size: int = 1) -> bytes | None:
    """Read from an arbitrary FxPakPro address."""
    try:
        with grpc.insecure_channel(host) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.ReadMemoryRequest(
                requestAddress=addr,
                requestAddressSpace=pb.AddressSpace.FxPakPro,
                size=size,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=uri, request=request)
            )
            return bytes(response.response.data)
    except Exception as e:
        print(f"  Read error at ${addr:06X}: {e}")
    return None


def send_command(host: str, uri: str, cmd: int, p1: int = 0, p2: int = 0, p3: int = 0) -> int | None:
    """Send a command to the hook inbox and wait for it to be processed.

    Returns the result code, or None on error/timeout.
    """
    # Write params first, then command byte (so hook sees consistent state)
    inbox_data = bytes([cmd, p1, p2, p3 & 0xFF, (p3 >> 8) & 0xFF])
    # Write params at INBOX_COMMAND+1 first
    if not write_mailbox(host, uri, INBOX_COMMAND + 1, inbox_data[1:]):
        return None
    # Write command byte to trigger
    if not write_mailbox(host, uri, INBOX_COMMAND, bytes([cmd])):
        return None

    # Poll until command byte clears (hook sets it to 0 when done)
    for _ in range(20):
        time.sleep(0.05)
        data = read_mailbox(host, uri, INBOX_COMMAND, 1)
        if data and data[0] == 0x00:
            # Read result
            result = read_mailbox(host, uri, OUTBOX_RESULT, 1)
            if result:
                return result[0]
            return None
    print("  Timeout waiting for command to complete!")
    return None


def test_hook_alive(host: str, uri: str) -> bool:
    """Check if the hook is running by reading version byte and frame counter."""
    print("=" * 60)
    print("TEST: Hook alive check")
    print("=" * 60)

    data = read_mailbox(host, uri, 0, 8)
    if data is None:
        print("  FAIL: Could not read mailbox")
        return False

    version = data[OUTBOX_VERSION]
    frame_ctr = data[OUTBOX_FRAME_CTR] | (data[OUTBOX_FRAME_CTR + 1] << 8)
    music = data[OUTBOX_MUSIC]
    battle = data[OUTBOX_BATTLE]
    game_mode = data[OUTBOX_GAME_MODE]

    game_mode_names = {
        0xC0: "overworld/gameplay",
        0xC3: "menu/pause",
        0xC1: "battle setup",
    }
    mode_str = game_mode_names.get(game_mode, "transition/other")

    print(f"  Version byte:  0x{version:02X} (expected 0x{HOOK_VERSION:02X})")
    print(f"  Frame counter: {frame_ctr}")
    print(f"  Music track:   0x{music:02X}")
    print(f"  Battle state:  0x{battle:02X}")
    print(f"  Game mode:     0x{game_mode:02X} ({mode_str})")

    if version != HOOK_VERSION:
        print(f"  FAIL: Version mismatch! Hook may not be installed.")
        return False

    # Read frame counter again to check it's incrementing
    time.sleep(0.1)
    data2 = read_mailbox(host, uri, OUTBOX_FRAME_CTR, 2)
    if data2 is None:
        print("  FAIL: Could not re-read frame counter")
        return False
    frame_ctr2 = data2[0] | (data2[1] << 8)
    delta = (frame_ctr2 - frame_ctr) & 0xFFFF

    print(f"  Frame counter (100ms later): {frame_ctr2} (delta={delta})")

    if delta == 0:
        print("  WARN: Frame counter not incrementing. Game may be paused?")
    else:
        print(f"  OK: Hook is running (~{delta * 10} frames/sec)")

    return True


def test_state_dump(host: str, uri: str) -> bool:
    """Send a state dump command and display the results."""
    print()
    print("=" * 60)
    print("TEST: State dump (CMD $09)")
    print("=" * 60)

    result = send_command(host, uri, CMD_STATE_DUMP)
    if result is None:
        print("  FAIL: No response from hook")
        return False

    if result != RESULT_OK:
        print(f"  FAIL: Unexpected result 0x{result:02X}")
        return False

    print(f"  Result: OK (0x{result:02X})")

    # Read the state dump region (OUTBOX_CONSUMABLES through end of MAX_HP)
    dump_size = (OUTBOX_MAX_HP + 10) - OUTBOX_CONSUMABLES  # 10B for 5 chars × 2B
    data = read_mailbox(host, uri, OUTBOX_CONSUMABLES, dump_size)
    if data is None:
        print("  FAIL: Could not read state dump")
        return False

    # Parse consumables (30 bytes: 29 usable + Waste Basket)
    off = 0
    consumables = data[off:off + 30]
    filled = [f"0x{b:02X}" for b in consumables if b != 0xFF]
    print(f"  Consumables: {len(filled)}/30 slots used")
    if filled:
        print(f"    Items: {', '.join(filled)}")

    # Equipment (30 bytes)
    off = OUTBOX_EQUIPMENT - OUTBOX_CONSUMABLES
    equipment = data[off:off + 30]
    filled = [f"0x{b:02X}" for b in equipment if b != 0xFF]
    print(f"  Equipment: {len(filled)}/30 slots used")
    if filled:
        print(f"    Items: {', '.join(filled)}")

    # Key items (30 bytes, expanded by randomizer)
    off = OUTBOX_KEY_ITEMS - OUTBOX_CONSUMABLES
    key_items = data[off:off + 30]
    filled = [f"0x{b:02X}" for b in key_items if b != 0xFF]
    print(f"  Key items: {len(filled)}/30 slots used")
    if filled:
        print(f"    Items: {', '.join(filled)}")

    # Coins (2 bytes LE)
    off = OUTBOX_COINS - OUTBOX_CONSUMABLES
    coins = data[off] | (data[off + 1] << 8)
    print(f"  Coins: {coins}")

    # FP (WRAM order: coins → FP_cur → FP_max → frog_coins)
    off = OUTBOX_CURRENT_FP - OUTBOX_CONSUMABLES
    cur_fp = data[off]
    off = OUTBOX_MAX_FP - OUTBOX_CONSUMABLES
    max_fp = data[off]
    print(f"  FP: {cur_fp}/{max_fp}")

    # Frog coins (2 bytes LE)
    off = OUTBOX_FROG_COINS - OUTBOX_CONSUMABLES
    frog_coins = data[off] | (data[off + 1] << 8)
    print(f"  Frog coins: {frog_coins}")

    # Star pieces (read directly from BW-RAM $30D5 = FxPakPro $E030D5)
    star_data = read_fxpak(host, uri, 0xE030D5, 1)
    if star_data:
        print(f"  Star pieces: {star_data[0]}/7")

    # Character HP
    off = OUTBOX_CUR_HP - OUTBOX_CONSUMABLES
    char_names = ["Mario", "Toadstool", "Bowser", "Geno", "Mallow"]
    print("  Character HP:")
    for i in range(5):
        cur_hp = data[off + i * 2] | (data[off + i * 2 + 1] << 8)
        max_off = OUTBOX_MAX_HP - OUTBOX_CONSUMABLES
        max_hp = data[max_off + i * 2] | (data[max_off + i * 2 + 1] << 8)
        print(f"    {char_names[i]}: {cur_hp}/{max_hp}")

    return True


def test_monitor(host: str, uri: str, duration: int = 10) -> None:
    """Continuously monitor the mailbox for a few seconds."""
    print()
    print("=" * 60)
    print(f"MONITOR: Watching mailbox for {duration} seconds")
    print("=" * 60)

    start = time.time()
    prev_music = None
    prev_battle = None
    prev_frame = None

    prev_mode = None

    while time.time() - start < duration:
        data = read_mailbox(host, uri, 0, 8)
        if data is None:
            continue

        music = data[OUTBOX_MUSIC]
        battle = data[OUTBOX_BATTLE]
        frame = data[OUTBOX_FRAME_CTR] | (data[OUTBOX_FRAME_CTR + 1] << 8)
        game_mode = data[OUTBOX_GAME_MODE]

        changed = False
        if music != prev_music:
            print(f"  [{time.time() - start:.1f}s] Music changed: 0x{music:02X}")
            prev_music = music
            changed = True
        if battle != prev_battle:
            state = "IN BATTLE" if battle else "not in battle"
            print(f"  [{time.time() - start:.1f}s] Battle state: 0x{battle:02X} ({state})")
            prev_battle = battle
            changed = True
        if game_mode != prev_mode:
            mode_names = {0xC0: "overworld", 0xC3: "menu", 0xC1: "battle setup"}
            print(f"  [{time.time() - start:.1f}s] Game mode: 0x{game_mode:02X} ({mode_names.get(game_mode, '?')})")
            prev_mode = game_mode
            changed = True
        if not changed and prev_frame is not None:
            delta = (frame - prev_frame) & 0xFFFF
            if delta == 0:
                print(f"  [{time.time() - start:.1f}s] WARNING: Frame counter stalled at {frame}")

        prev_frame = frame
        time.sleep(0.25)

    print(f"  Done monitoring. Final frame counter: {frame}")


def diagnose_hook_failure(host: str, uri: str) -> None:
    """Run diagnostics when the hook appears dead."""
    print()
    print("=" * 60)
    print("DIAGNOSTIC: SRAM write/read test")
    print("=" * 60)

    # Test 1: Can we write and read back from the mailbox location?
    test_val = bytes([0xAA])
    print(f"  Writing 0xAA to $E03E04 (version byte location)...")
    if write_mailbox(host, uri, OUTBOX_VERSION, test_val):
        time.sleep(0.1)
        readback = read_mailbox(host, uri, OUTBOX_VERSION, 1)
        if readback:
            print(f"  Read back: 0x{readback[0]:02X}")
            if readback[0] == 0xAA:
                print("  SRAM write/read OK — FxPakPro can access this location")
                print("  → Hook is NOT writing here. Issue is in the SNES-side code.")
            elif readback[0] == 0x00:
                print("  Read back 0x00 — game or SA-1 may be clearing this area!")
            elif readback[0] == HOOK_VERSION:
                print("  Read back hook version! Hook IS running but may be intermittent.")
            else:
                print(f"  Unexpected value — something is writing to this location")

    # Test 2: Read the ROM patches to verify they're present
    print()
    print("=" * 60)
    print("DIAGNOSTIC: ROM patch verification")
    print("=" * 60)
    # Read NMI vectors from ROM via FxPakPro
    # Native NMI vector at SNES $00:FFEA
    rom_data = None
    try:
        with grpc.insecure_channel(host) as ch:
            stub = sni.DeviceMemoryStub(ch)
            # Read $00:FFE0-$FFFF (vector table area, 32 bytes)
            request = pb.ReadMemoryRequest(
                requestAddress=0x00FFE0,
                requestAddressSpace=pb.AddressSpace.SnesLoROM,
                size=32,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=uri, request=request)
            )
            rom_data = bytes(response.response.data)
    except Exception as e:
        print(f"  Could not read ROM vectors: {e}")

    if rom_data and len(rom_data) >= 32:
        # $FFE0-$FFE3: our trampoline (should be 5C 00 F0 D5)
        tramp = rom_data[0:4]
        print(f"  $FFE0 trampoline: {tramp.hex()} (expect 5c00f0d5)")

        # $FFEA-$FFEB: native NMI vector (should be E0 FF)
        nmi_native = rom_data[0x0A:0x0C]
        print(f"  $FFEA native NMI: {nmi_native.hex()} (expect e0ff)")

        # $FFFA-$FFFB: emu NMI vector (should be E0 FF)
        nmi_emu = rom_data[0x1A:0x1C]
        print(f"  $FFFA emu NMI:    {nmi_emu.hex()} (expect e0ff)")

    # Test 3: Read first 16 bytes of hook code at $D5:F000
    hook_data = None
    try:
        with grpc.insecure_channel(host) as ch:
            stub = sni.DeviceMemoryStub(ch)
            request = pb.ReadMemoryRequest(
                requestAddress=0xD5F000,
                requestAddressSpace=pb.AddressSpace.SnesLoROM,
                size=16,
            )
            response = stub.SingleRead(
                pb.SingleReadMemoryRequest(uri=uri, request=request)
            )
            hook_data = bytes(response.response.data)
    except Exception as e:
        print(f"  Could not read hook code: {e}")

    if hook_data:
        print(f"  $D5:F000 hook:    {hook_data.hex()}")
        print(f"    (expect: 18fbc230... = CLC;XCE;REP#$30;...)")

    # Test 4: Scan nearby SRAM pages for version byte
    print()
    print("=" * 60)
    print("DIAGNOSTIC: Scanning SRAM for hook version byte")
    print("=" * 60)
    # Check if the hook is writing to a different BMAPS page
    for page in range(8):
        addr = 0xE00000 + page * 0x2000 + 0x1E00  # offset $1E00 within each 8KB page
        data = None
        try:
            with grpc.insecure_channel(host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.ReadMemoryRequest(
                    requestAddress=addr,
                    requestAddressSpace=pb.AddressSpace.FxPakPro,
                    size=8,
                )
                response = stub.SingleRead(
                    pb.SingleReadMemoryRequest(uri=uri, request=request)
                )
                data = bytes(response.response.data)
        except Exception:
            pass

        if data:
            # Check if version byte (offset +4) is $01
            if data[4] == HOOK_VERSION:
                print(f"  FOUND at ${addr:06X} (BMAPS page {page}): {data.hex()}")
            elif any(b != 0 for b in data[:6]):
                print(f"  Non-zero at ${addr:06X} (BMAPS page {page}): {data.hex()}")

    # Test 5: Write/readback at multiple BW-RAM locations to find safe zones
    print()
    print("=" * 60)
    print("DIAGNOSTIC: BW-RAM write persistence test")
    print("=" * 60)
    print("  Writing 0xBB to test locations, waiting 200ms, reading back...")
    test_addrs = [
        (0xE02000, "BW-RAM $2000 (BMAPS=1 page start)"),
        (0xE02800, "BW-RAM $2800"),
        (0xE03000, "BW-RAM $3000"),
        (0xE03800, "BW-RAM $3800"),
        (0xE03E00, "BW-RAM $3E00 (current mailbox)"),
        (0xE03F00, "BW-RAM $3F00"),
        (0xE03FF0, "BW-RAM $3FF0 (AP counter area)"),
        (0xE00100, "BW-RAM $0100 (page 0)"),
        (0xE00F00, "BW-RAM $0F00 (page 0 end)"),
        (0xE04100, "BW-RAM $4100 (page 2)"),
        (0xE06100, "BW-RAM $6100 (page 3)"),
        (0xE07F00, "BW-RAM $7F00 (page 3 end)"),
    ]
    # Write test pattern to all locations
    for addr, desc in test_addrs:
        try:
            with grpc.insecure_channel(host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.WriteMemoryRequest(
                    requestAddress=addr,
                    requestAddressSpace=pb.AddressSpace.FxPakPro,
                    data=bytes([0xBB]),
                )
                stub.SingleWrite(
                    pb.SingleWriteMemoryRequest(uri=uri, request=request)
                )
        except Exception:
            pass

    time.sleep(0.3)

    # Read back
    for addr, desc in test_addrs:
        try:
            with grpc.insecure_channel(host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.ReadMemoryRequest(
                    requestAddress=addr,
                    requestAddressSpace=pb.AddressSpace.FxPakPro,
                    size=1,
                )
                response = stub.SingleRead(
                    pb.SingleReadMemoryRequest(uri=uri, request=request)
                )
                val = response.response.data[0]
                status = "SURVIVED" if val == 0xBB else f"CLEARED (0x{val:02X})"
                print(f"  ${addr:06X} {desc}: {status}")
        except Exception as e:
            print(f"  ${addr:06X} {desc}: ERROR {e}")

    print()
    print("Locations marked SURVIVED are safe for the mailbox.")


def main() -> None:
    parser = argparse.ArgumentParser(description="NMI Hook Mailbox Test")
    parser.add_argument("--host", default="localhost:8191", help="SNI host:port")
    parser.add_argument("--monitor", type=int, default=0,
                        help="Monitor duration in seconds (0=skip)")
    parser.add_argument("--give-item", nargs=2, type=lambda x: int(x, 0),
                        metavar=("TYPE", "ID"),
                        help="Give item: type (0=con,1=eq,2=key) and item ID (hex)")
    parser.add_argument("--set-coins", type=int, metavar="AMOUNT",
                        help="Set coins to this amount")
    parser.add_argument("--add-coins", type=int, metavar="AMOUNT",
                        help="Add coins (caps at 999)")
    parser.add_argument("--add-frog-coins", type=int, metavar="AMOUNT",
                        help="Add frog coins (caps at 999)")
    parser.add_argument("--add-star", action="store_true",
                        help="Increment star piece counter (caps at 7)")
    parser.add_argument("--recruit", type=int, metavar="CHAR",
                        help="Recruit character (0=Mario,1=Toadstool,2=Bowser,3=Geno,4=Mallow)")
    parser.add_argument("--learn-spell", nargs=2, type=int,
                        metavar=("CHAR", "BIT"),
                        help="Learn spell: character index (0-4) and spell bit (0-31)")
    parser.add_argument("--heal", action="store_true", help="Heal all characters")
    args = parser.parse_args()

    print("NMI Cooperative Hook — Mailbox Test")
    print("=" * 60)

    uri = find_device(args.host)
    if not uri:
        print("Failed to connect. Is SNI running?")
        sys.exit(1)
    print(f"Connected: {uri}")

    # Test 1: Hook alive
    if not test_hook_alive(args.host, uri):
        print("\nHook does not appear to be running. Running diagnostics...")
        diagnose_hook_failure(args.host, uri)
        sys.exit(1)

    # Test 2: State dump
    test_state_dump(args.host, uri)

    # Optional: Give item
    if args.give_item:
        item_type, item_id = args.give_item
        type_names = {0: "consumable", 1: "equipment", 2: "key item"}
        print(f"\nGiving {type_names.get(item_type, '?')} 0x{item_id:02X}...")
        result = send_command(args.host, uri, CMD_GIVE_ITEM, p1=item_type, p2=item_id)
        if result == RESULT_OK:
            print("  OK: Item added to inventory!")
        elif result == RESULT_INV_FULL:
            print("  FAIL: Inventory full!")
        else:
            print(f"  ERROR: Unexpected result 0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Set coins
    if args.set_coins is not None:
        print(f"\nSetting coins to {args.set_coins}...")
        result = send_command(args.host, uri, CMD_SET_COINS, p3=args.set_coins)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Add coins
    if args.add_coins is not None:
        print(f"\nAdding {args.add_coins} coins...")
        result = send_command(args.host, uri, CMD_ADD_COINS, p3=args.add_coins)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Add frog coins
    if args.add_frog_coins is not None:
        print(f"\nAdding {args.add_frog_coins} frog coins...")
        result = send_command(args.host, uri, CMD_ADD_FROG_COINS, p3=args.add_frog_coins)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Add star piece
    if args.add_star:
        print("\nAdding star piece...")
        result = send_command(args.host, uri, CMD_ADD_STAR_PIECE)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Recruit character
    if args.recruit is not None:
        char_names = {0: "Mario", 1: "Toadstool", 2: "Bowser", 3: "Geno", 4: "Mallow"}
        print(f"\nRecruiting {char_names.get(args.recruit, '?')} (char={args.recruit})...")
        result = send_command(args.host, uri, CMD_RECRUIT_CHAR, p2=args.recruit)
        if result == RESULT_OK:
            print("  OK!")
        elif result == RESULT_INV_FULL:
            print("  FAIL: No empty party slot!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Learn spell
    if args.learn_spell:
        char_idx, spell_bit = args.learn_spell
        char_names = {0: "Mario", 1: "Toadstool", 2: "Bowser", 3: "Geno", 4: "Mallow"}
        print(f"\nTeaching {char_names.get(char_idx, '?')} spell bit {spell_bit}...")
        result = send_command(args.host, uri, CMD_LEARN_SPELL, p1=char_idx, p2=spell_bit)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Heal
    if args.heal:
        print("\nHealing all characters...")
        result = send_command(args.host, uri, CMD_HEAL)
        if result == RESULT_OK:
            print("  OK!")
        else:
            print(f"  ERROR: result=0x{result:02X}" if result else "  ERROR: No response")

    # Optional: Monitor
    if args.monitor > 0:
        test_monitor(args.host, uri, args.monitor)

    print("\nDone!")


if __name__ == "__main__":
    main()
