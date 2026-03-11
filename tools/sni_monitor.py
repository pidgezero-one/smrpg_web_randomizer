#!/usr/bin/env python3
"""
Phase 3A: SMRPG Real-Time Debug Monitor

Connects to SNI / FXPak Pro and displays live game state:
  - Current area and party composition
  - Character stats (HP, level, attack, defense, etc.)
  - Event flags (decoded to human-readable names)
  - Coins, frog coins, hidden chests
  - Battle state (when in battle)

Refreshes every ~100ms. Uses the address spaces determined by Phase 1 testing.

Usage:
    source tools/.venv/bin/activate
    python tools/sni_monitor.py [--host HOST:PORT] [--refresh MS]

Requirements:
    pip install snirk
"""

import argparse
import asyncio
import os
import sys
import time

import grpc
from snirk.sni import sni_pb2 as pb
from snirk.sni import sni_pb2_grpc as sni

from smrpg_memmap import (
    AREA_NAMES,
    CHARACTER_NAMES,
    EVENT_FLAGS,
    parse_character_stats,
    parse_event_flags,
)


class SNIReader:
    """Low-level SNI memory reader supporting multiple address spaces."""

    def __init__(self, channel_str: str):
        self.channel_str = channel_str
        self.device_uri: str | None = None

    async def connect(self) -> bool:
        """Find device and cache URI."""
        try:
            with grpc.insecure_channel(self.channel_str) as ch:
                stub = sni.DevicesStub(ch)
                response = stub.ListDevices(pb.DevicesRequest(kinds=[]))
                if response and response.devices:
                    self.device_uri = response.devices[0].uri
                    return True
        except Exception:
            pass
        return False

    def _read_sync(
        self, address: int, size: int,
        address_space: int = pb.AddressSpace.FxPakPro,
        mapping: int = pb.MemoryMapping.SA1,
    ) -> bytes | None:
        """Synchronous single read."""
        try:
            with grpc.insecure_channel(self.channel_str) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.ReadMemoryRequest(
                    requestAddress=address,
                    requestAddressSpace=address_space,
                    requestMemoryMapping=mapping,
                    size=size,
                )
                response = stub.SingleRead(
                    pb.SingleReadMemoryRequest(
                        uri=self.device_uri, request=request
                    )
                )
                return bytes(response.response.data)
        except Exception:
            return None

    def multi_read_sync(
        self, reads: list[tuple[int, int, int]],
    ) -> list[bytes | None]:
        """Batch read: list of (address, size, address_space) tuples.

        Uses gRPC MultiRead for efficiency when all reads share the same
        address space, falls back to individual reads otherwise.
        """
        if not reads:
            return []

        # Group by address space for batched reads
        results = [None] * len(reads)

        # Try MultiRead for each group
        by_space: dict[int, list[tuple[int, int, int, int]]] = {}
        for idx, (addr, size, space) in enumerate(reads):
            by_space.setdefault(space, []).append((idx, addr, size, space))

        for space, group in by_space.items():
            try:
                with grpc.insecure_channel(self.channel_str) as ch:
                    stub = sni.DeviceMemoryStub(ch)
                    requests = [
                        pb.ReadMemoryRequest(
                            requestAddress=addr,
                            requestAddressSpace=space,
                            requestMemoryMapping=pb.MemoryMapping.SA1,
                            size=size,
                        )
                        for _, addr, size, _ in group
                    ]
                    response = stub.MultiRead(
                        pb.MultiReadMemoryRequest(
                            uri=self.device_uri, requests=requests
                        )
                    )
                    for (idx, _, _, _), resp in zip(group, response.responses):
                        results[idx] = bytes(resp.data)
            except Exception:
                # Fall back to individual reads
                for idx, addr, size, _ in group:
                    results[idx] = self._read_sync(addr, size, space)

        return results


class GameState:
    """Parsed SMRPG game state from memory reads."""

    def __init__(self):
        self.characters: list[dict] = []
        self.coins: int = 0
        self.frog_coins: int = 0
        self.current_area: int = 0
        self.area_name: str = "Unknown"
        self.party: list[str] = []
        self.party_count: int = 0
        self.event_flags: dict[str, bool] = {}
        self.hidden_chests: int = 0
        self.boss_victories: int = 0
        self.menu_flags: int = 0
        self.battle_formation: int = 0
        self.map_location: int = 0
        self.read_errors: list[str] = []
        self.timestamp: float = 0


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def format_state(state: GameState) -> str:
    """Format game state for terminal display."""
    lines = []
    lines.append("=" * 70)
    lines.append(f"  SMRPG Debug Monitor — {time.strftime('%H:%M:%S')}")
    lines.append("=" * 70)

    # Area and party
    lines.append("")
    lines.append(f"  Area: {state.area_name} (ID: {state.current_area})")
    lines.append(f"  Map Location: {state.map_location}")
    lines.append(f"  Party ({state.party_count}): {', '.join(state.party) if state.party else '(unknown)'}")
    lines.append(f"  Coins: {state.coins}   Frog Coins: {state.frog_coins}   "
                 f"Hidden Chests: {state.hidden_chests}   Boss Wins: {state.boss_victories}")

    # Battle
    if state.battle_formation > 0:
        lines.append(f"  ** IN BATTLE ** Formation: {state.battle_formation}")

    # Characters
    lines.append("")
    lines.append("  " + "-" * 66)
    lines.append(f"  {'Name':<10} {'Lv':>3} {'HP':>8} {'Spd':>4} {'Atk':>4} "
                 f"{'Def':>4} {'MgA':>4} {'MgD':>4} {'Exp':>6}")
    lines.append("  " + "-" * 66)
    for char in state.characters:
        if char["max_hp"] > 0:
            lines.append(
                f"  {char['name']:<10} {char['level']:>3} "
                f"{char['current_hp']:>3}/{char['max_hp']:<4} "
                f"{char['speed']:>4} {char['attack']:>4} "
                f"{char['defense']:>4} {char['mg_attack']:>4} "
                f"{char['mg_defense']:>4} {char['experience']:>6}"
            )

    # Menu unlocks
    lines.append("")
    menu_items = []
    if state.menu_flags & 0x01: menu_items.append("Map")
    if state.menu_flags & 0x02: menu_items.append("Star Piece")
    if state.menu_flags & 0x04: menu_items.append("Switch")
    if state.menu_flags & 0x08: menu_items.append("Beetlemania")
    lines.append(f"  Menus: {', '.join(menu_items) if menu_items else '(none)'}")

    # Event flags (show set ones)
    set_flags = [name for name, val in state.event_flags.items() if val]
    if set_flags:
        lines.append("")
        lines.append(f"  Event Flags ({len(set_flags)} set):")

        # Categorize flags for readability
        bosses = [f for f in set_flags if "Defeated" in f or "Boss" in f]
        areas = [f for f in set_flags if "Liberated" in f]
        maps = [f for f in set_flags if f.startswith("Map:")]
        other = [f for f in set_flags
                 if f not in bosses and f not in areas and f not in maps]

        if bosses:
            lines.append(f"    Bosses: {', '.join(bosses)}")
        if areas:
            lines.append(f"    Areas:  {', '.join(areas)}")
        if maps:
            lines.append(f"    Maps:   {', '.join(m.replace('Map: ', '') for m in maps)}")
        if other:
            for flag in other[:10]:
                lines.append(f"    - {flag}")
            if len(other) > 10:
                lines.append(f"    ... and {len(other) - 10} more")

    # Errors
    if state.read_errors:
        lines.append("")
        lines.append("  Read Errors:")
        for err in state.read_errors:
            lines.append(f"    ! {err}")

    lines.append("")
    lines.append("  Press Ctrl+C to stop")
    return "\n".join(lines)


async def read_game_state(
    reader: SNIReader,
    use_abus_bwram: bool = True,
    use_abus_iram: bool = True,
    use_mirror: bool = False,
) -> GameState:
    """Read all game state in one batch."""
    state = GameState()
    state.timestamp = time.time()

    # Build read list: (address, size, address_space)
    FX = pb.AddressSpace.FxPakPro
    AB = pb.AddressSpace.SnesABus

    reads = [
        (0xF6F800, 0xB9, FX),   # 0: character block
        (0xF6F8B9, 0x02, FX),   # 1: coins
        (0xF6F8BB, 0x02, FX),   # 2: frog coins
        (0xF50048, 0x02, FX),   # 3: battle formation
        (0xF509E5, 0x02, FX),   # 4: map location
    ]

    # BW-RAM reads
    if use_abus_bwram:
        base = 0x40 if use_mirror else 0x00
        reads.append((base * 0x010000 + 0x7040, 0x60, AB))  # 5: event flags
        reads.append((base * 0x010000 + 0x7062, 0x01, AB))  # 6: menu flags
        reads.append((base * 0x010000 + 0x70C8, 0x01, AB))  # 7: hidden chests
        reads.append((base * 0x010000 + 0x70E3, 0x01, AB))  # 8: boss victories
    else:
        reads.extend([(0, 0, FX)] * 4)  # placeholders

    # IRAM reads
    if use_abus_iram:
        base = 0x40 if use_mirror else 0x00
        reads.append((base * 0x010000 + 0x3030, 0x02, AB))  # 9: current area
        reads.append((base * 0x010000 + 0x3032, 0x0E, AB))  # 10: party slots
        reads.append((base * 0x010000 + 0x303F, 0x01, AB))  # 11: party count
    else:
        reads.extend([(0, 0, FX)] * 3)  # placeholders

    # Execute all reads
    results = reader.multi_read_sync(reads)

    # Parse character block
    if results[0] is not None:
        for i in range(5):
            try:
                stats = parse_character_stats(results[0], i)
                state.characters.append(stats)
            except Exception:
                state.characters.append({
                    "name": CHARACTER_NAMES.get(i, "?"), "level": 0,
                    "current_hp": 0, "max_hp": 0, "speed": 0, "attack": 0,
                    "defense": 0, "mg_attack": 0, "mg_defense": 0,
                    "experience": 0, "weapon": 0, "armor": 0, "accessory": 0,
                })
    else:
        state.read_errors.append("Character block read failed")

    # Parse coins
    if results[1] is not None:
        state.coins = int.from_bytes(results[1], "little")
    else:
        state.read_errors.append("Coins read failed")

    # Parse frog coins
    if results[2] is not None:
        state.frog_coins = int.from_bytes(results[2], "little")

    # Parse battle formation
    if results[3] is not None:
        state.battle_formation = int.from_bytes(results[3], "little")

    # Parse map location
    if results[4] is not None:
        state.map_location = int.from_bytes(results[4], "little")

    # Parse event flags
    if use_abus_bwram and results[5] is not None:
        state.event_flags = parse_event_flags(results[5])
    elif use_abus_bwram:
        state.read_errors.append("Event flags read failed")

    # Parse menu flags
    if use_abus_bwram and results[6] is not None:
        state.menu_flags = results[6][0]

    # Parse hidden chests
    if use_abus_bwram and results[7] is not None:
        state.hidden_chests = results[7][0]

    # Parse boss victories
    if use_abus_bwram and results[8] is not None:
        state.boss_victories = results[8][0]

    # Parse current area
    if use_abus_iram and results[9] is not None:
        state.current_area = int.from_bytes(results[9], "little")
        state.area_name = AREA_NAMES.get(state.current_area,
                                          f"Unknown ({state.current_area})")
    elif use_abus_iram:
        state.read_errors.append("Current area read failed")

    # Parse party slots
    if use_abus_iram and results[10] is not None:
        party_data = results[10]
        state.party = []
        for i in range(min(5, len(party_data))):
            char_id = party_data[i]
            if char_id < 5:
                state.party.append(CHARACTER_NAMES[char_id])
    elif use_abus_iram:
        state.read_errors.append("Party slots read failed")

    # Parse party count
    if use_abus_iram and results[11] is not None:
        state.party_count = results[11][0]

    return state


async def monitor_loop(
    reader: SNIReader,
    refresh_ms: int,
    use_abus_bwram: bool,
    use_abus_iram: bool,
    use_mirror: bool,
):
    """Main monitoring loop."""
    while True:
        try:
            state = await read_game_state(
                reader, use_abus_bwram, use_abus_iram, use_mirror
            )
            clear_screen()
            print(format_state(state))
            await asyncio.sleep(refresh_ms / 1000.0)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nError: {e}")
            await asyncio.sleep(1)


async def main():
    parser = argparse.ArgumentParser(
        description="SMRPG Real-Time Debug Monitor"
    )
    parser.add_argument(
        "--host", default="localhost:8191",
        help="SNI host:port (default: localhost:8191)"
    )
    parser.add_argument(
        "--refresh", type=int, default=100,
        help="Refresh interval in ms (default: 100)"
    )
    parser.add_argument(
        "--no-bwram", action="store_true",
        help="Skip BW-RAM reads (if Phase 1 showed they fail)"
    )
    parser.add_argument(
        "--no-iram", action="store_true",
        help="Skip IRAM reads (if Phase 1 showed they fail)"
    )
    parser.add_argument(
        "--mirror", action="store_true",
        help="Use $40 bank mirror for BW-RAM/IRAM access"
    )
    args = parser.parse_args()

    reader = SNIReader(args.host)

    print("Connecting to SNI...")
    if not await reader.connect():
        print(f"Failed to connect to SNI at {args.host}")
        print("Make sure SNI is running and FXPak Pro is connected.")
        sys.exit(1)
    print(f"Connected: {reader.device_uri}")
    print("Starting monitor... (Ctrl+C to stop)")
    await asyncio.sleep(0.5)

    try:
        await monitor_loop(
            reader,
            args.refresh,
            use_abus_bwram=not args.no_bwram,
            use_abus_iram=not args.no_iram,
            use_mirror=args.mirror,
        )
    except KeyboardInterrupt:
        print("\nMonitor stopped.")


if __name__ == "__main__":
    asyncio.run(main())
