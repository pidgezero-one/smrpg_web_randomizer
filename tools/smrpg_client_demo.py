"""Interactive demo for the unified SMRPG SNI Client.

Shows game state, logs check events, and accepts commands for item delivery.

Usage:
    source tools/.venv/bin/activate
    python tools/smrpg_client_demo.py [--host HOST:PORT] [--refresh MS]

Commands:
    give <type> <id>    Give item (type: 0=con, 1=eq, 2=key; id: hex)
    coins <amount>      Add coins
    frogcoins <amount>  Add frog coins
    star                Add star piece
    recruit <char>      Recruit character (mario/peach/bowser/geno/mallow)
    heal                Heal all characters
    dump                Request inventory state dump
    status              Show current game state summary
    checks              Show all completed checks
    quit                Exit
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
import time

# Add tools dir for sibling imports
_tools_dir = os.path.dirname(os.path.abspath(__file__))
if _tools_dir not in sys.path:
    sys.path.insert(0, _tools_dir)

from smrpg_client import (
    SmrpgClient, CheckEvent, VarEvent, RoomEvent, CommandEvent, GameMode,
    GameModeEvent, CurrencyChangeEvent, FpChangeEvent,
    InventoryChangeEvent, HpChangeEvent, StarPieceEvent,
    ITEM_NAMES,
)

# Character name → ID mapping for recruit command
CHAR_NAME_TO_ID = {
    "mario": 0, "peach": 1, "bowser": 2, "geno": 3, "mallow": 4,
    "toadstool": 1,  # alias
}


def format_timestamp(ts: float) -> str:
    """Format a timestamp as HH:MM:SS."""
    t = time.localtime(ts)
    return f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"


def _item_name(item_id: int) -> str:
    """Resolve an item ID to its display name."""
    return ITEM_NAMES.get(item_id, f"0x{item_id:02X}")


def print_header(client: SmrpgClient) -> None:
    """Print the two-line game state header on fixed top rows."""
    mode = client.game_mode
    mode_str = mode.name if mode != GameMode.UNKNOWN else f"0x{client.game_mode_byte:02X}"

    battle_str = " [BATTLE]" if client.in_battle else ""
    hook_ver = f"v{client._version_byte}" if client.hook_alive else "DEAD"
    party_str = ", ".join(client.party) if client.party else "(none)"
    area_str = client.current_area

    line1 = (
        f"[{mode_str}{battle_str}] "
        f"Area: {area_str} | "
        f"Party: {party_str} | "
        f"Hook: {hook_ver}"
    )

    # Build HP string for active party members
    hp_parts = []
    for ch in client.characters:
        if ch["max_hp"] > 0:
            hp_parts.append(f"{ch['name'][:3]}:{ch['current_hp']}/{ch['max_hp']}")
    hp_str = " ".join(hp_parts)

    line2 = (
        f"Coins: {client.coins} | "
        f"Frog: {client.frog_coins} | "
        f"Stars: {client.star_pieces} | "
        f"FP: {client.current_fp}/{client.max_fp} | "
        f"Inv: {client.consumable_count}c/{client.equipment_count}e/{client.key_item_count}k | "
        f"HP: {hp_str}"
    )

    print(
        f"\033[s"
        f"\033[1;1H\033[K{line1}"
        f"\033[2;1H\033[K{line2}"
        f"\033[3;1H\033[K"        # blank row 3 as separator
        f"\033[u",
        end="", flush=True,
    )


def on_check(event: CheckEvent) -> None:
    """Handle a check event — print it to the log."""
    ts = format_timestamp(event.timestamp)
    print(f"\r\033[K  [{ts}] CHECK [{event.check_type.value.upper()}] {event.name}")
    print("> ", end="", flush=True)


def on_var(event: VarEvent) -> None:
    """Handle a variable change event — print it to the log."""
    ts = format_timestamp(event.timestamp)
    action = "SET" if event.value else "CLR"
    print(f"\r\033[K  [{ts}] VAR {action}: {event.var_name}")
    print("> ", end="", flush=True)


def on_room(event: RoomEvent) -> None:
    """Handle a room change event — print it to the log."""
    ts = format_timestamp(event.timestamp)
    print(f"\r\033[K  [{ts}] ROOM [{event.prev_room_id}] {event.prev_room_name} -> [{event.room_id}] {event.room_name}")
    print("> ", end="", flush=True)


def on_command(event: CommandEvent) -> None:
    """Handle a command event — print it to the log (skip STATE_DUMP to reduce noise)."""
    if event.command_name == "STATE_DUMP":
        return
    ts = format_timestamp(event.timestamp)
    status = "OK" if event.success else "FAIL"
    print(f"\r\033[K  [{ts}] CMD {event.command_name} p1={event.param1} p2={event.param2} [{status}]")
    print("> ", end="", flush=True)


def on_game_mode(event: GameModeEvent) -> None:
    ts = format_timestamp(event.timestamp)
    old = event.prev_mode.name if event.prev_mode != GameMode.UNKNOWN else f"0x{event.prev_mode_byte:02X}"
    new = event.mode.name if event.mode != GameMode.UNKNOWN else f"0x{event.mode_byte:02X}"
    print(f"\r\033[K  [{ts}] MODE {old} -> {new}")
    print("> ", end="", flush=True)


def on_currency(event: CurrencyChangeEvent) -> None:
    ts = format_timestamp(event.timestamp)
    sign = "+" if event.delta > 0 else ""
    label = "COINS" if event.currency == "coins" else "FROG COINS"
    print(f"\r\033[K  [{ts}] {label}: {event.old_value} -> {event.new_value} ({sign}{event.delta})")
    print("> ", end="", flush=True)


def on_fp(event: FpChangeEvent) -> None:
    ts = format_timestamp(event.timestamp)
    delta = event.new_fp - event.old_fp
    sign = "+" if delta > 0 else ""
    parts = [f"FP: {event.old_fp} -> {event.new_fp} ({sign}{delta})"]
    if event.max_fp != event.old_max_fp:
        parts.append(f"Max FP: {event.old_max_fp} -> {event.max_fp}")
    print(f"\r\033[K  [{ts}] {' | '.join(parts)}")
    print("> ", end="", flush=True)


def on_inventory(event: InventoryChangeEvent) -> None:
    ts = format_timestamp(event.timestamp)
    parts = []
    if event.added:
        parts.append(f"added [{', '.join(_item_name(x) for x in event.added)}]")
    if event.removed:
        parts.append(f"removed [{', '.join(_item_name(x) for x in event.removed)}]")
    label = event.inventory_type.upper()
    print(f"\r\033[K  [{ts}] INV [{label}] {' '.join(parts)} (total: {event.new_count})")
    print("> ", end="", flush=True)


def on_hp(event: HpChangeEvent) -> None:
    ts = format_timestamp(event.timestamp)
    delta = event.new_hp - event.old_hp
    sign = "+" if delta > 0 else ""
    print(f"\r\033[K  [{ts}] HEAL {event.char_name}: {event.old_hp} -> {event.new_hp}/{event.max_hp} ({sign}{delta})")
    print("> ", end="", flush=True)


def on_star_piece(event: StarPieceEvent) -> None:
    ts = format_timestamp(event.timestamp)
    print(f"\r\033[K  [{ts}] STAR PIECE: {event.old_count} -> {event.new_count}")
    print("> ", end="", flush=True)


async def handle_command(client: SmrpgClient, line: str) -> None:
    """Parse and execute a user command."""
    parts = line.strip().split()
    if not parts:
        return

    cmd = parts[0].lower()

    if cmd == "give":
        if len(parts) < 3:
            print("  Usage: give <type:0=con,1=eq,2=key> <id:hex>")
            return
        try:
            item_type = int(parts[1], 0)
            item_id = int(parts[2], 0)
        except ValueError:
            print("  Usage: give <type:0-2> <id:hex>")
            return
        type_names = {0: "consumable", 1: "equipment", 2: "key item"}
        type_name = type_names.get(item_type, f"type {item_type}")
        print(f"  Giving {type_name} 0x{item_id:02X}...", end="", flush=True)
        ok = await client.give_item(item_type, item_id)
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "coins":
        if len(parts) < 2:
            print("  Usage: coins <amount>")
            return
        try:
            amount = int(parts[1], 0)
        except ValueError:
            print("  Usage: coins <amount>")
            return
        print(f"  Adding {amount} coins...", end="", flush=True)
        ok = await client.add_coins(amount)
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "frogcoins":
        if len(parts) < 2:
            print("  Usage: frogcoins <amount>")
            return
        try:
            amount = int(parts[1], 0)
        except ValueError:
            print("  Usage: frogcoins <amount>")
            return
        print(f"  Adding {amount} frog coins...", end="", flush=True)
        ok = await client.add_frog_coins(amount)
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "star":
        print("\n  Adding star piece...", end="", flush=True)
        ok = await client.add_star_piece()
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "recruit":
        if len(parts) < 2:
            print(f"\n  Usage: recruit <mario|peach|bowser|geno|mallow>")
            return
        char_name = parts[1].lower()
        char_id = CHAR_NAME_TO_ID.get(char_name)
        if char_id is None:
            print(f"  Unknown character: {parts[1]}")
            print(f"  Valid: {', '.join(CHAR_NAME_TO_ID.keys())}")
            return
        print(f"  Recruiting {char_name}...", end="", flush=True)
        ok = await client.recruit_character(char_id)
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "heal":
        print("  Healing all...", end="", flush=True)
        ok = await client.heal()
        print(f" {'OK' if ok else 'FAILED'}")

    elif cmd == "dump":
        print("  Requesting state dump...", end="", flush=True)
        result = await client.request_state_dump()
        if result is None:
            print(" FAILED")
        else:
            print(" OK")
            print(f"    Coins: {result['coins']}  Frog: {result['frog_coins']}  "
                  f"FP: {result['current_fp']}/{result['max_fp']}")
            print(f"    Consumables ({len(result['consumables'])}): "
                  f"{[f'0x{x:02X}' for x in result['consumables']]}")
            print(f"    Equipment ({len(result['equipment'])}): "
                  f"{[f'0x{x:02X}' for x in result['equipment']]}")
            print(f"    Key Items ({len(result['key_items'])}): "
                  f"{[f'0x{x:02X}' for x in result['key_items']]}")
            char_names = ["Mario", "Peach", "Bowser", "Geno", "Mallow"]
            for i, name in enumerate(char_names):
                print(f"    {name}: HP {result['cur_hp'][i]}/{result['max_hp'][i]}")

    elif cmd == "status":
        summary = client.state_summary()
        for k, v in summary.items():
            print(f"    {k}: {v}")
        chars = client.characters
        if chars:
            print("    characters:")
            for ch in chars:
                print(f"      {ch['name']}: "
                      f"HP:{ch['current_hp']}/{ch['max_hp']}")

    elif cmd == "checks":
        completed = {k: v for k, v in client.checks.items() if v}
        if completed:
            print(f"  Completed checks ({len(completed)}):")
            for k in sorted(completed.keys()):
                print(f"    - {k}")
        else:
            print("  No checks completed yet.")

    elif cmd == "debug":
        print("  Debug poll — raw read results:")
        await client.debug_poll()
        # Show parsed outbox details
        print(f"    Version byte: 0x{client._version_byte:02X} (expect 0x02 for IRAM support)")
        print(f"    Area ID raw: {client._area_id} (0x{client._area_id:04X})")
        raw_party = client._party_slot_data
        if raw_party:
            hex_str = " ".join(f"{b:02X}" for b in raw_party)
            print(f"    Party slots raw: [{hex_str}] (expect char IDs 0-4, FF=empty)")
        print(f"    Party count: {client._party_count}")

    elif cmd == "presence":
        print("  Reading NPC presence region ($6D20-$6F1F)...")
        data = client.read_npc_presence()
        if data is None:
            print("  FAILED")
        else:
            print(f"  NPC presence: {len(data)} bytes from $E02D20")
            # Print hex dump in 16-byte rows with offset
            for row in range(0, len(data), 16):
                chunk = data[row:row + 16]
                hex_str = " ".join(f"{b:02X}" for b in chunk)
                snes_addr = 0x6D20 + row
                print(f"    ${snes_addr:04X}: {hex_str}")

    elif cmd in ("quit", "exit", "q"):
        print("  Goodbye!")
        sys.exit(0)

    else:
        print(f"  Unknown command: {cmd}")
        print("  Commands: give, coins, frogcoins, star, recruit, heal, dump, status, checks, debug, presence, quit")


async def stdin_reader() -> str:
    """Read a line from stdin without blocking the event loop."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, sys.stdin.readline)


async def main() -> None:
    parser = argparse.ArgumentParser(description="SMRPG SNI Client Demo")
    parser.add_argument("--host", default="localhost:8191", help="SNI host:port")
    parser.add_argument("--refresh", type=int, default=200, help="Poll interval in ms")
    parser.add_argument("--spoiler", help="Path to spoiler.json for accurate check names")
    args = parser.parse_args()

    print("SMRPG Client Demo")
    print(f"Connecting to SNI at {args.host}...")

    client = SmrpgClient(args.host)
    if args.spoiler:
        client.load_check_mapping(args.spoiler)
        chest_ct = len(client._chest_check_table) if client._chest_check_table else 0
        npc_ct = len(client._npc_presence_check_table) if client._npc_presence_check_table else 0
        hill_ct = len(client._booster_hill_checks) if client._booster_hill_checks else 0
        print(f"Loaded check mapping from {args.spoiler}")
        print(f"  Chest checks: {chest_ct}, NPC presence checks: {npc_ct}, Booster Hill checks: {hill_ct}")
    client.on_check(on_check)
    client.on_var_change(on_var)
    client.on_room_change(on_room)
    client.on_command(on_command)
    client.on_game_mode_change(on_game_mode)
    client.on_currency_change(on_currency)
    client.on_fp_change(on_fp)
    client.on_inventory_change(on_inventory)
    client.on_hp_change(on_hp)
    client.on_star_piece_change(on_star_piece)

    connected = await client.connect()
    if not connected:
        print("Failed to connect to SNI or NMI hook not alive.")
        print("Make sure:")
        print("  1. SNI is running")
        print("  2. FxPak Pro is connected")
        print("  3. ROM with NMI hook patch is loaded")
        print()
        print("Attempting to continue anyway (hook may initialize later)...")
        # Try connecting without hook verification
        if not await client._reader.connect():
            print("Cannot find any SNI device. Exiting.")
            return
        print("Device found, but hook not verified. Polling will start.")
    else:
        print("Connected! Hook is alive.")

    # Clear screen: rows 1-2 = header, row 3 = blank, row 4 = separator, row 5+ = log/input
    print("\033[2J\033[H")  # clear screen, cursor to top
    print()  # row 1 placeholder (header line 1 will overwrite)
    print()  # row 2 placeholder (header line 2 will overwrite)
    print()  # row 3 blank separator
    print("-" * 72)
    print("Commands: give, coins, frogcoins, star, recruit, heal, dump, status, checks, quit")
    print("Events will appear automatically.")
    print("> ", end="", flush=True)

    # Run poll loop and stdin reader concurrently
    async def poll_loop() -> None:
        while True:
            try:
                await client.poll()
                print_header(client)
            except Exception as e:
                print(f"\r\033[K  Poll error: {e}")
                print("> ", end="", flush=True)
            await asyncio.sleep(args.refresh / 1000.0)

    async def input_loop() -> None:
        while True:
            try:
                line = await stdin_reader()
                if not line:
                    # EOF
                    break
                print(f"\033[A\033[K> {line.strip()}", flush=True)  # re-echo the command clearly
                await handle_command(client, line)
                print("> ", end="", flush=True)
            except (EOFError, KeyboardInterrupt):
                break

    poll_task = asyncio.create_task(poll_loop())
    input_task = asyncio.create_task(input_loop())

    # Wait for either to finish (input_loop exits on quit/EOF)
    done, pending = await asyncio.wait(
        [poll_task, input_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted.")
