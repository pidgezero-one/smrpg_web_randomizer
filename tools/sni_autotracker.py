#!/usr/bin/env python3
"""
Phase 3B: SMRPG Auto-Tracker Data Provider

Reads randomizer-relevant game state via SNI / FXPak Pro and exposes it
over a local WebSocket for tracker integration.

Tracked state:
  - Boss defeats and area liberation (progression)
  - Characters recruited
  - Key items obtained
  - World map accessibility
  - Star pieces collected
  - Hidden chest count
  - Menu unlocks

Output: JSON over WebSocket at ws://localhost:8585 (configurable).
Also supports --stdout mode for piping to other tools.

Usage:
    source tools/.venv/bin/activate
    python tools/sni_autotracker.py [--host HOST:PORT] [--ws-port PORT]
    python tools/sni_autotracker.py --stdout  # JSON to stdout

Requirements:
    pip install snirk
    For WebSocket mode: pip install websockets
"""

import argparse
import asyncio
import json
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
    """Low-level SNI memory reader."""

    def __init__(self, channel_str: str):
        self.channel_str = channel_str
        self.device_uri: str | None = None

    async def connect(self) -> bool:
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

    def multi_read_sync(
        self, reads: list[tuple[int, int, int]],
    ) -> list[bytes | None]:
        """Batch read: list of (address, size, address_space) tuples."""
        if not reads:
            return []

        results = [None] * len(reads)
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
                pass

        return results


# =============================================================================
# Tracker state definitions - what the auto-tracker cares about
# =============================================================================

# Boss checks: (flag_byte_offset, flag_bit, tracker_key, display_name)
BOSS_CHECKS = [
    (0x42, 0, "mushroom_kingdom_boss", "Hammer Bros / Mushroom Kingdom"),
    (0x15, 2, "sewer_boss", "Belome 1 / Kero Sewers"),
    (0x43, 6, "forest_boss", "Bowyer / Forest Maze"),
    (0x16, 5, "mines_boss_1", "Croco 2 / Moleville Mines"),
    (0x16, 3, "mines_boss_2", "Punchinello / Moleville Mines"),
    (0x13, 4, "tower_boss_1", "Knife Guy & Grate Guy / Booster Tower"),
    (0x4B, 5, "tower_boss_2", "Booster / Booster Tower"),
    (0x14, 2, "keep_boss_2", "Bundt / Marrymore"),
    (0x18, 6, "ship_midboss", "King Calamari / Sunken Ship"),
    (0x18, 7, "ship_boss", "Johnny / Sunken Ship"),
    (0x46, 0, "seaside_boss", "Yaridovich / Seaside Town"),
    (0x4A, 0, "temple_boss", "Belome 2 / Belome Temple"),
    (0x4C, 3, "bean_valley_boss", "Megasmilax / Bean Valley"),
    (0x1F, 5, "nimbus_mid_boss", "Birdo / Nimbus Land"),
    (0x50, 2, "nimbus_boss", "Valentina / Nimbus Land"),
    (0x3E, 0, "volcano_midboss", "Czar Dragon / Barrel Volcano"),
    (0x3D, 7, "volcano_boss", "Axem Rangers / Barrel Volcano"),
    (0x53, 6, "keep_boss_1", "Magikoopa / Bowser's Keep"),
    (0x53, 7, "keep_boss_3", "Boomer / Bowser's Keep"),
    (0x12, 0, "factory_boss", "Smithy / Factory"),
    (0x4F, 7, "abyss_boss_1", "Count Down / Factory"),
    (0x56, 0, "abyss_boss_2", "Cloaker & Domino / Factory"),

    # Dojo
    (0x4A, 2, "dojo_1", "Jinx 1 / Dojo"),
    (0x4A, 3, "dojo_2", "Jinx 2 / Dojo"),
    (0x4A, 4, "dojo_3", "Jinx 3 / Dojo"),
    (0x4A, 5, "dojo_4", "Culex / Dojo"),
]

# Area liberation checks
AREA_CHECKS = [
    (0x42, 0, "mk_liberated", "Mushroom Kingdom Liberated"),
    (0x0D, 3, "bw_liberated", "Bandits Way Liberated"),
    (0x43, 6, "forest_liberated", "Forest Liberated"),
    (0x0C, 6, "marrymore_liberated", "Marrymore Liberated"),
    (0x18, 7, "ship_liberated", "Sunken Ship Liberated"),
    (0x46, 0, "seaside_liberated", "Seaside Liberated"),
    (0x1F, 4, "nimbus_liberated", "Nimbus Land Liberated"),
    (0x3D, 7, "volcano_liberated", "Barrel Volcano Liberated"),
    (0x09, 7, "yoster_liberated_1", "Yoster Isle Liberated 1"),
    (0x1E, 2, "yoster_liberated_2", "Yoster Isle Liberated 2"),
]

# Star piece tracking
STAR_PIECE_CHECKS = [
    (0x41, 1, "star_mimic3", "Mimic 3 Star Piece"),
    (0x41, 2, "star_statue_keeper", "Statue Keeper Star Piece"),
    (0x41, 3, "star_tower_boss", "Tower Boss 1 Star Piece"),
    (0x41, 4, "star_lands_end_cloud", "Land's End Cloud Star Piece"),
    (0x52, 4, "star_battle_door", "Battle Door Star Piece"),
    (0x55, 3, "star_hill_checked", "Star Hill Checked"),
]

# World map discovery
MAP_CHECKS = [
    (0x25, 1, "map_marios_pad", "Mario's Pad"),
    (0x25, 2, "map_mushroom_way", "Mushroom Way"),
    (0x25, 3, "map_mushroom_kingdom", "Mushroom Kingdom"),
    (0x25, 4, "map_bandits_way", "Bandits Way"),
    (0x26, 2, "map_rose_town", "Rose Town"),
    (0x26, 3, "map_forest_maze", "Forest Maze"),
    (0x26, 4, "map_pipe_vault", "Pipe Vault"),
    (0x26, 5, "map_yoster_isle", "Yoster Isle"),
    (0x26, 6, "map_moleville", "Moleville"),
    (0x26, 7, "map_booster_pass", "Booster Pass"),
    (0x27, 0, "map_booster_tower", "Booster Tower"),
    (0x27, 1, "map_marrymore", "Marrymore"),
    (0x27, 2, "map_star_hill", "Star Hill"),
    (0x27, 3, "map_seaside_town", "Seaside Town"),
    (0x27, 4, "map_sea", "Sea"),
    (0x27, 5, "map_sunken_ship", "Sunken Ship"),
    (0x27, 6, "map_lands_end", "Land's End"),
    (0x27, 7, "map_monstro_town", "Monstro Town"),
    (0x28, 0, "map_bean_valley", "Bean Valley"),
    (0x28, 1, "map_nimbus_land", "Nimbus Land"),
    (0x28, 2, "map_barrel_volcano", "Barrel Volcano"),
    (0x28, 3, "map_vista_hill", "Vista Hill"),
    (0x28, 4, "map_booster_hill", "Booster Hill"),
    (0x28, 5, "map_gate", "Gate"),
    (0x28, 6, "map_casino", "Casino"),
]

# Key item / prize checks
KEY_ITEM_CHECKS = [
    (0x19, 0, "casino_prize", "Casino Prize Won"),
    (0x55, 5, "cricket_pie", "Cricket Pie Exchanged"),
    (0x1E, 4, "shiny_stone", "Shiny Stone Traded"),
    (0x4E, 5, "gave_seed", "Gave Seed"),
    (0x4E, 6, "gave_fertilizer", "Gave Fertilizer"),
    (0x52, 0, "super_jump_1", "Super Jump Prize 1"),
    (0x52, 2, "super_jump_2", "Super Jump Prize 2"),
    (0x59, 4, "goomba_thumpin_1", "Goomba Thumpin Prize 1"),
    (0x59, 5, "goomba_thumpin_2", "Goomba Thumpin Prize 2"),
    (0x59, 6, "knife_guy_prize", "Knife Guy Prize"),
    (0x17, 4, "minecart_cleared", "Minecart Cleared"),
    (0x0D, 7, "booster_hill_cleared", "Booster Hill Cleared"),
    (0x13, 6, "tower_opened", "Tower Opened"),
    (0x13, 7, "tower_char_recruited", "Tower Character Recruited"),
]

# Win conditions
WIN_CONDITION_CHECKS = [
    (0x11, 6, "wc_star_pieces", "Win Condition: Star Pieces"),
    (0x11, 7, "wc_monstro_door", "Win Condition: Monstro Door"),
    (0x59, 0, "wc_smithy_hunt", "Win Condition: Smithy Boss Hunt"),
    (0x46, 7, "wc_alt_star", "Alternate Star Piece Win Condition"),
]


def check_flag(data: bytes, byte_offset: int, bit: int) -> bool:
    """Check a single flag bit in event flag data."""
    if byte_offset < len(data):
        return bool(data[byte_offset] & (1 << bit))
    return False


def build_tracker_state(
    event_data: bytes | None,
    char_data: bytes | None,
    coins_data: bytes | None,
    frog_coins_data: bytes | None,
    area_data: bytes | None,
    party_data: bytes | None,
    party_count_data: bytes | None,
    hidden_chest_data: bytes | None,
    boss_victory_data: bytes | None,
    menu_data: bytes | None,
) -> dict:
    """Build the full tracker state dict from raw memory reads."""
    state = {
        "timestamp": time.time(),
        "connected": True,
    }

    # Bosses
    bosses = {}
    if event_data:
        for byte_off, bit, key, name in BOSS_CHECKS:
            bosses[key] = {
                "name": name,
                "defeated": check_flag(event_data, byte_off, bit),
            }
    state["bosses"] = bosses

    # Areas
    areas = {}
    if event_data:
        for byte_off, bit, key, name in AREA_CHECKS:
            areas[key] = {
                "name": name,
                "liberated": check_flag(event_data, byte_off, bit),
            }
    state["areas"] = areas

    # Star pieces
    star_pieces = {}
    if event_data:
        for byte_off, bit, key, name in STAR_PIECE_CHECKS:
            star_pieces[key] = {
                "name": name,
                "collected": check_flag(event_data, byte_off, bit),
            }
        state["star_piece_count"] = sum(
            1 for v in star_pieces.values() if v["collected"]
        )
    state["star_pieces"] = star_pieces

    # World map
    world_map = {}
    if event_data:
        for byte_off, bit, key, name in MAP_CHECKS:
            world_map[key] = {
                "name": name,
                "discovered": check_flag(event_data, byte_off, bit),
            }
    state["world_map"] = world_map

    # Key items
    key_items = {}
    if event_data:
        for byte_off, bit, key, name in KEY_ITEM_CHECKS:
            key_items[key] = {
                "name": name,
                "obtained": check_flag(event_data, byte_off, bit),
            }
    state["key_items"] = key_items

    # Win conditions
    win_conditions = {}
    if event_data:
        for byte_off, bit, key, name in WIN_CONDITION_CHECKS:
            win_conditions[key] = {
                "name": name,
                "active": check_flag(event_data, byte_off, bit),
            }
    state["win_conditions"] = win_conditions

    # Characters
    characters = {}
    if char_data:
        for i in range(5):
            try:
                stats = parse_character_stats(char_data, i)
                characters[CHARACTER_NAMES[i].lower()] = {
                    "name": stats["name"],
                    "level": stats["level"],
                    "current_hp": stats["current_hp"],
                    "max_hp": stats["max_hp"],
                    "in_party": stats["max_hp"] > 0,
                }
            except Exception:
                pass
    state["characters"] = characters

    # Party composition
    if party_data:
        party = []
        for i in range(min(5, len(party_data))):
            char_id = party_data[i]
            if char_id < 5:
                party.append(CHARACTER_NAMES[char_id])
        state["party"] = party
    else:
        state["party"] = []

    if party_count_data:
        state["party_count"] = party_count_data[0]
    else:
        state["party_count"] = 0

    # Currencies
    if coins_data:
        state["coins"] = int.from_bytes(coins_data, "little")
    else:
        state["coins"] = 0

    if frog_coins_data:
        state["frog_coins"] = int.from_bytes(frog_coins_data, "little")
    else:
        state["frog_coins"] = 0

    # Current area
    if area_data:
        area_id = int.from_bytes(area_data, "little")
        state["current_area"] = {
            "id": area_id,
            "name": AREA_NAMES.get(area_id, f"Unknown ({area_id})"),
        }
    else:
        state["current_area"] = {"id": -1, "name": "Unknown"}

    # Hidden chests
    if hidden_chest_data:
        state["hidden_chests"] = hidden_chest_data[0]
    else:
        state["hidden_chests"] = 0

    # Boss victories
    if boss_victory_data:
        state["boss_victory_count"] = boss_victory_data[0]
    else:
        state["boss_victory_count"] = 0

    # Menu unlocks
    if menu_data:
        val = menu_data[0]
        state["menus"] = {
            "map": bool(val & 0x01),
            "star_piece": bool(val & 0x02),
            "switch": bool(val & 0x04),
            "beetlemania": bool(val & 0x08),
        }
    else:
        state["menus"] = {}

    return state


async def read_tracker_state(
    reader: SNIReader,
    use_abus_bwram: bool = True,
    use_abus_iram: bool = True,
    use_mirror: bool = False,
) -> dict:
    """Read and build tracker state."""
    FX = pb.AddressSpace.FxPakPro
    AB = pb.AddressSpace.SnesABus

    base = 0x40 if use_mirror else 0x00

    reads = [
        (0xF6F800, 0xB9, FX),   # 0: character block
        (0xF6F8B9, 0x02, FX),   # 1: coins
        (0xF6F8BB, 0x02, FX),   # 2: frog coins
    ]

    # BW-RAM
    if use_abus_bwram:
        reads.append((base * 0x010000 + 0x7040, 0x60, AB))  # 3: event flags
        reads.append((base * 0x010000 + 0x70C8, 0x01, AB))  # 4: hidden chests
        reads.append((base * 0x010000 + 0x70E3, 0x01, AB))  # 5: boss victories
        reads.append((base * 0x010000 + 0x7062, 0x01, AB))  # 6: menu flags
    else:
        reads.extend([(0, 0, FX)] * 4)

    # IRAM
    if use_abus_iram:
        reads.append((base * 0x010000 + 0x3030, 0x02, AB))  # 7: current area
        reads.append((base * 0x010000 + 0x3032, 0x0E, AB))  # 8: party slots
        reads.append((base * 0x010000 + 0x303F, 0x01, AB))  # 9: party count
    else:
        reads.extend([(0, 0, FX)] * 3)

    results = reader.multi_read_sync(reads)

    return build_tracker_state(
        event_data=results[3] if use_abus_bwram else None,
        char_data=results[0],
        coins_data=results[1],
        frog_coins_data=results[2],
        area_data=results[7] if use_abus_iram else None,
        party_data=results[8] if use_abus_iram else None,
        party_count_data=results[9] if use_abus_iram else None,
        hidden_chest_data=results[4] if use_abus_bwram else None,
        boss_victory_data=results[5] if use_abus_bwram else None,
        menu_data=results[6] if use_abus_bwram else None,
    )


# =============================================================================
# WebSocket server
# =============================================================================

connected_clients: set = set()


async def ws_handler(websocket, path=None):
    """Handle a new WebSocket connection."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Clients can send "ping" to check connection
            if message.strip().lower() == "ping":
                await websocket.send(json.dumps({"type": "pong"}))
    except Exception:
        pass
    finally:
        connected_clients.discard(websocket)


async def broadcast(data: dict):
    """Send state to all connected WebSocket clients."""
    if not connected_clients:
        return
    message = json.dumps(data)
    disconnected = set()
    for ws in connected_clients:
        try:
            await ws.send(message)
        except Exception:
            disconnected.add(ws)
    connected_clients.difference_update(disconnected)


async def tracker_loop(
    reader: SNIReader,
    refresh_ms: int,
    use_abus_bwram: bool,
    use_abus_iram: bool,
    use_mirror: bool,
    stdout_mode: bool,
):
    """Main tracker loop - reads state and broadcasts."""
    last_state_json = ""

    while True:
        try:
            state = await read_tracker_state(
                reader, use_abus_bwram, use_abus_iram, use_mirror
            )
            state_json = json.dumps(state, sort_keys=True)

            # Only broadcast/print on state change
            if state_json != last_state_json:
                last_state_json = state_json
                if stdout_mode:
                    print(json.dumps(state, indent=2))
                    print("---")
                    sys.stdout.flush()
                else:
                    await broadcast(state)

            await asyncio.sleep(refresh_ms / 1000.0)
        except KeyboardInterrupt:
            break
        except Exception as e:
            error_state = {
                "timestamp": time.time(),
                "connected": False,
                "error": str(e),
            }
            if stdout_mode:
                print(json.dumps(error_state, indent=2))
                sys.stdout.flush()
            else:
                await broadcast(error_state)
            await asyncio.sleep(1)


async def main():
    parser = argparse.ArgumentParser(
        description="SMRPG Auto-Tracker Data Provider"
    )
    parser.add_argument(
        "--host", default="localhost:8191",
        help="SNI host:port (default: localhost:8191)"
    )
    parser.add_argument(
        "--ws-port", type=int, default=8585,
        help="WebSocket server port (default: 8585)"
    )
    parser.add_argument(
        "--refresh", type=int, default=200,
        help="Refresh interval in ms (default: 200)"
    )
    parser.add_argument(
        "--stdout", action="store_true",
        help="Output JSON to stdout instead of WebSocket"
    )
    parser.add_argument(
        "--no-bwram", action="store_true",
        help="Skip BW-RAM reads"
    )
    parser.add_argument(
        "--no-iram", action="store_true",
        help="Skip IRAM reads"
    )
    parser.add_argument(
        "--mirror", action="store_true",
        help="Use $40 bank mirror for BW-RAM/IRAM"
    )
    args = parser.parse_args()

    reader = SNIReader(args.host)

    print("Connecting to SNI...")
    if not await reader.connect():
        print(f"Failed to connect to SNI at {args.host}")
        sys.exit(1)
    print(f"Connected: {reader.device_uri}")

    if args.stdout:
        print("Running in stdout mode (JSON output)...")
        await tracker_loop(
            reader, args.refresh,
            use_abus_bwram=not args.no_bwram,
            use_abus_iram=not args.no_iram,
            use_mirror=args.mirror,
            stdout_mode=True,
        )
    else:
        try:
            import websockets
        except ImportError:
            print("WebSocket mode requires 'websockets' package.")
            print("  pip install websockets")
            print("Or use --stdout mode for JSON output.")
            sys.exit(1)

        print(f"Starting WebSocket server on ws://localhost:{args.ws_port}")
        print("Clients can connect to receive auto-tracker state updates.")
        print("Press Ctrl+C to stop.")

        async with websockets.serve(ws_handler, "localhost", args.ws_port):
            await tracker_loop(
                reader, args.refresh,
                use_abus_bwram=not args.no_bwram,
                use_abus_iram=not args.no_iram,
                use_mirror=args.mirror,
                stdout_mode=False,
            )


if __name__ == "__main__":
    asyncio.run(main())
