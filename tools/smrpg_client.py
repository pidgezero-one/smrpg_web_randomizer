"""Unified SMRPG SNI Client for Archipelago Integration.

Combines check detection (event flags + recruitment), item delivery
(NMI hook mailbox), and game state tracking into a single async API.

Usage:
    from smrpg_client import SmrpgClient, CheckType

    client = SmrpgClient("localhost:8191")
    client.on_check(lambda evt: print(f"CHECK: {evt.name}"))
    await client.connect()
    await client.run()

Requirements:
    pip install snirk
"""

from __future__ import annotations

import asyncio
import os
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import Callable

# Add repo root to path for randomizer.data imports (run from repo root)
_repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)
# Add tools dir for sibling imports
_tools_dir = os.path.dirname(os.path.abspath(__file__))
if _tools_dir not in sys.path:
    sys.path.insert(0, _tools_dir)

import grpc
from snirk.sni import sni_pb2 as pb, sni_pb2_grpc as sni

from smrpg_memmap import CHARACTER_NAMES
from smrpg_check_data import (
    ROOM_NAMES,
    FLAG_NAMES,
    CHECK_CONDITIONS,
    COMPOUND_CHECKS,
    check_flag,
    AP_REGION_LOWER_ADDR,
    AP_REGION_LOWER_SIZE,
    AP_REGION_EVENT_ADDR,
    AP_REGION_EVENT_SIZE,
    AP_REGION_CHEST_ADDR,
    AP_REGION_CHEST_SIZE,
    AP_LOWER_CHECKS,
    AP_EVENT_CHECKS,
    AP_CHEST_CHECKS,
)
from randomizer.data.nmi_hook import (
    MAILBOX_FXPAK_BASE,
    OUTBOX_MUSIC,
    OUTBOX_BATTLE,
    OUTBOX_FRAME_CTR,
    OUTBOX_VERSION,
    OUTBOX_RESULT,
    OUTBOX_GAME_MODE,
    OUTBOX_AREA_ID,
    OUTBOX_PARTY_SLOTS,
    OUTBOX_PARTY_COUNT,
    OUTBOX_CONSUMABLES,
    OUTBOX_EQUIPMENT,
    OUTBOX_KEY_ITEMS,
    OUTBOX_COINS,
    OUTBOX_CURRENT_FP,
    OUTBOX_MAX_FP,
    OUTBOX_FROG_COINS,
    OUTBOX_CUR_HP,
    OUTBOX_MAX_HP,
    INBOX_COMMAND,
    INBOX_PARAM1,
    INBOX_PARAM2,
    INBOX_PARAM3,
    CMD_IDLE,
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


# =============================================================================
# Address constants
# =============================================================================
#
# On real SA-1 hardware with FxPak Pro:
#   - FxPakPro SRAM ($E0xxxx) = BW-RAM: WORKS
#   - FxPakPro WRAM ($F5/$F6xxxx): returns open bus (0x55) — SA-1 blocks access
#   - SnesABus ($00:xxxx / $40:xxxx): fails entirely
#
# So ALL reads go through FxPakPro SRAM. For WRAM data (coins, characters),
# we use the hook's CMD_STATE_DUMP. IRAM (party, area) is read from the
# hook's per-frame outbox where available, otherwise from state dump.
#
# BW-RAM address conversion (BMAPS=1 window):
#   SNES $00:xxxx (where xxxx in $6000-$7FFF) → BW-RAM = xxxx - $4000
#   FxPakPro SRAM = $E00000 + BW-RAM offset

FX = pb.AddressSpace.FxPakPro


def _snes_to_fxpak_bwram(snes_addr: int) -> int:
    """Convert SNES A-Bus BW-RAM window address to FxPakPro SRAM address.

    BMAPS=1: $00:6000-$7FFF → BW-RAM $2000-$3FFF → FxPakPro $E02000-$E03FFF
    """
    return 0xE00000 + (snes_addr - 0x4000)


# BW-RAM read regions for AP check detection (from smrpg_check_data)
BWRAM_LOWER = (AP_REGION_LOWER_ADDR, AP_REGION_LOWER_SIZE)       # Key items, NPC triggers
BWRAM_EVENT_FLAGS = (AP_REGION_EVENT_ADDR, AP_REGION_EVENT_SIZE)  # Event flags (96 bytes)
BWRAM_CHESTS = (AP_REGION_CHEST_ADDR, AP_REGION_CHEST_SIZE)      # Treasure chests

# Additional BW-RAM reads for game state
BWRAM_HIDDEN_CHESTS = (_snes_to_fxpak_bwram(0x70C8), 0x01)
BWRAM_BOSS_VICTORIES = (_snes_to_fxpak_bwram(0x70E3), 0x01)
BWRAM_MENU_FLAGS = (_snes_to_fxpak_bwram(0x7062), 0x01)
BWRAM_BOOSTER_HILL_CTR = (_snes_to_fxpak_bwram(0x70B1), 0x01)


# =============================================================================
# Types
# =============================================================================

class GameMode(IntEnum):
    """Game mode derived from NMI handler bank byte at $7E:000B."""
    OVERWORLD = 0xC0        # In-level exploration
    BATTLE_SETUP = 0xC1     # Battle initialization
    MENU = 0xC3             # Pause menu
    UNKNOWN = 0xFF          # Transition or unrecognized


class CheckType(str, Enum):
    """Category of an Archipelago location check."""
    FLAG = "flag"
    CHEST = "chest"
    KEY_ITEM = "key_item"
    EVENT = "event"
    BOSS = "boss"
    RECRUITMENT = "recruitment"


@dataclass
class CheckEvent:
    """Fired when a check location is completed."""
    check_type: CheckType
    key: str
    name: str
    timestamp: float


@dataclass
class VarEvent:
    """Fired when a non-check flag variable changes."""
    var_name: str
    byte_offset: int
    bit: int
    value: bool
    timestamp: float


@dataclass
class RoomEvent:
    """Fired when the player enters a new room."""
    room_id: int
    room_name: str
    prev_room_id: int
    prev_room_name: str
    timestamp: float


@dataclass
class CommandEvent:
    """Fired when a command is sent to/from the SNES via the NMI hook mailbox."""
    command: int
    command_name: str
    param1: int
    param2: int
    success: bool
    timestamp: float


@dataclass
class GameModeEvent:
    """Fired when the game mode changes (e.g. overworld → battle)."""
    prev_mode: GameMode
    prev_mode_byte: int
    mode: GameMode
    mode_byte: int
    timestamp: float


@dataclass
class CurrencyChangeEvent:
    """Fired when coins or frog coins change."""
    currency: str          # "coins" or "frog_coins"
    old_value: int
    new_value: int
    delta: int
    timestamp: float


@dataclass
class FpChangeEvent:
    """Fired when current FP or max FP changes."""
    old_fp: int
    new_fp: int
    max_fp: int
    old_max_fp: int
    timestamp: float


@dataclass
class InventoryChangeEvent:
    """Fired when an inventory slot changes."""
    inventory_type: str    # "consumable", "equipment", "key_item"
    added: list[int]       # item IDs added
    removed: list[int]     # item IDs removed
    new_count: int         # new inventory size
    timestamp: float


@dataclass
class HpChangeEvent:
    """Fired when a character's HP changes in the overworld."""
    char_index: int
    char_name: str
    old_hp: int
    new_hp: int
    max_hp: int
    timestamp: float


@dataclass
class StarPieceEvent:
    """Fired when the star piece count changes."""
    old_count: int
    new_count: int
    timestamp: float


def _check_type_from_name(name: str) -> CheckType:
    """Derive CheckType from AP location name prefix."""
    if name.startswith("Chest"):
        return CheckType.CHEST
    if name.startswith("Key Item"):
        return CheckType.KEY_ITEM
    if name.startswith("Boss"):
        return CheckType.BOSS
    if name.startswith("Event"):
        return CheckType.EVENT
    return CheckType.FLAG


# Reverse lookup: variable name → (byte_offset, bit) in event flag region
_FLAG_NAME_TO_POS: dict[str, tuple[int, int]] = {
    name: (byte_off, bit) for (byte_off, bit), name in FLAG_NAMES.items()
}

# Recruitment character mapping
_RECRUIT_CHARS = {0: "Mario", 1: "Peach", 2: "Bowser", 3: "Geno", 4: "Mallow"}


def _format_class_name(name: str) -> str:
    """Convert CamelCase class name to readable format: 'MushroomKingdomFreeShopItem' → 'Mushroom Kingdom Free Shop Item'."""
    import re as _re
    return _re.sub(r"(?<!^)(?=[A-Z])", " ", name)


# =============================================================================
# Item name lookup (static across all seeds)
# =============================================================================

ITEM_NAMES: dict[int, str] = {}
try:
    from randomizer.data.items.items import ITEMS as _ITEMS_COLLECTION
    for _item in _ITEMS_COLLECTION.items:
        ITEM_NAMES[_item.item_id] = _item.name
except ImportError:
    pass  # smrpgpatchbuilder not installed — names unavailable, fall back to hex


def _item_name(item_id: int) -> str:
    """Resolve an item ID to its display name, falling back to hex."""
    return ITEM_NAMES.get(item_id, f"0x{item_id:02X}")


# =============================================================================
# SNI Reader (async wrapper around gRPC)
# =============================================================================

class SNIReader:
    """Low-level SNI memory reader with batch support."""

    def __init__(self, host: str) -> None:
        self.host = host
        self.device_uri: str | None = None

    async def connect(self) -> bool:
        """Find the first SNI device and store its URI."""
        try:
            with grpc.insecure_channel(self.host) as ch:
                stub = sni.DevicesStub(ch)
                response = stub.ListDevices(pb.DevicesRequest(kinds=[]))
                if response and response.devices:
                    self.device_uri = response.devices[0].uri
                    return True
        except Exception:
            pass
        return False

    def multi_read(self, reads: list[tuple[int, int, int]]) -> list[bytes | None]:
        """Batch read: list of (address, size, address_space) tuples.

        Groups reads by address space and issues one MultiRead per group.
        Returns results in the same order as the input list.
        """
        if not reads:
            return []

        results: list[bytes | None] = [None] * len(reads)
        by_space: dict[int, list[tuple[int, int, int, int]]] = {}
        for idx, (addr, size, space) in enumerate(reads):
            by_space.setdefault(space, []).append((idx, addr, size, space))

        for space, group in by_space.items():
            try:
                with grpc.insecure_channel(self.host) as ch:
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
                            uri=self.device_uri,
                            requests=requests,
                        )
                    )
                    for (idx, _, _, _), resp in zip(group, response.responses):
                        results[idx] = bytes(resp.data)
            except Exception:
                pass  # results stay None for failed reads

        return results

    def write_fxpak(self, address: int, data: bytes) -> bool:
        """Write data to FxPakPro address space."""
        try:
            with grpc.insecure_channel(self.host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.WriteMemoryRequest(
                    requestAddress=address,
                    requestAddressSpace=FX,
                    data=data,
                )
                stub.SingleWrite(
                    pb.SingleWriteMemoryRequest(
                        uri=self.device_uri,
                        request=request,
                    )
                )
                return True
        except Exception:
            return False

    def read_fxpak(self, address: int, size: int) -> bytes | None:
        """Read from FxPakPro address space."""
        try:
            with grpc.insecure_channel(self.host) as ch:
                stub = sni.DeviceMemoryStub(ch)
                request = pb.ReadMemoryRequest(
                    requestAddress=address,
                    requestAddressSpace=FX,
                    size=size,
                )
                response = stub.SingleRead(
                    pb.SingleReadMemoryRequest(
                        uri=self.device_uri,
                        request=request,
                    )
                )
                return bytes(response.response.data)
        except Exception:
            return None


# =============================================================================
# SmrpgClient
# =============================================================================

class SmrpgClient:
    """Unified SMRPG client for Archipelago integration.

    Combines check detection, item delivery, and game state tracking.
    """

    def __init__(self, host: str = "localhost:8191") -> None:
        self._reader = SNIReader(host)
        self._check_callbacks: list[Callable[[CheckEvent], None]] = []
        self._var_callbacks: list[Callable[[VarEvent], None]] = []
        self._room_callbacks: list[Callable[[RoomEvent], None]] = []
        self._command_callbacks: list[Callable[[CommandEvent], None]] = []
        self._game_mode_callbacks: list[Callable[[GameModeEvent], None]] = []
        self._currency_callbacks: list[Callable[[CurrencyChangeEvent], None]] = []
        self._fp_callbacks: list[Callable[[FpChangeEvent], None]] = []
        self._inventory_callbacks: list[Callable[[InventoryChangeEvent], None]] = []
        self._hp_callbacks: list[Callable[[HpChangeEvent], None]] = []
        self._star_piece_callbacks: list[Callable[[StarPieceEvent], None]] = []

        # Current state (from mailbox outbox, per-frame)
        self._game_mode_byte: int = 0xFF
        self._battle_byte: int = 0
        self._music_byte: int = 0
        self._frame_counter: int = 0
        self._version_byte: int = 0
        self._result_byte: int = 0

        # BW-RAM state (read via FxPakPro SRAM, per-poll)
        self._lower_data: bytes = b""
        self._prev_lower_data: bytes | None = None
        self._event_data: bytes = b""
        self._prev_event_data: bytes | None = None
        self._chest_data: bytes = b""
        self._prev_chest_data: bytes | None = None
        self._hidden_chests: int = 0
        self._boss_victories: int = 0
        self._menu_flags: int = 0

        # WRAM state (from periodic CMD_STATE_DUMP via hook)
        self._coins: int = 0
        self._frog_coins: int = 0
        self._current_fp: int = 0
        self._max_fp: int = 0
        self._cur_hp: list[int] = [0] * 5
        self._max_hp: list[int] = [0] * 5

        # IRAM state (not directly readable — derived from state dump)
        self._party_slot_data: bytes = b""
        self._area_id: int = 0
        self._party_count: int = 0

        # Star pieces (read directly from BW-RAM)
        self._star_pieces: int = 0
        self._prev_star_pieces: int | None = None

        # Inventory lists (parsed from state dump, stored for header display)
        self._consumables: list[int] = []
        self._equipment: list[int] = []
        self._key_items: list[int] = []

        # Previous state for diffing (poll-level)
        self._prev_area_id: int | None = None
        self._prev_party_chars: list[int] | None = None
        self._prev_game_mode_byte: int | None = None

        # Previous state for diffing (state-dump-level)
        self._prev_coins: int | None = None
        self._prev_frog_coins: int | None = None
        self._prev_current_fp: int | None = None
        self._prev_max_fp: int | None = None
        self._prev_cur_hp: list[int] | None = None
        self._prev_max_hp: list[int] | None = None
        self._prev_consumables: list[int] | None = None
        self._prev_equipment: list[int] | None = None
        self._prev_key_items: list[int] | None = None

        # Completed checks: class_name → True (for flag-based and compound checks)
        self._checks: dict[str, bool] = {}
        # Also track recruitment checks
        for char_name in _RECRUIT_CHARS.values():
            self._checks[f"recruited_{char_name.lower()}"] = False

        self._first_poll: bool = True
        self._last_state_dump: float = 0.0
        self._state_dump_interval: float = 2.0  # seconds between state dumps

        # Loaded check bit mapping from spoiler (overrides AP_CHEST_CHECKS)
        self._chest_check_table: dict[tuple[int, int], list[tuple[str, bool]]] | None = None

        # NPC presence mapping from spoiler (NPC despawn-based checks)
        self._npc_presence_check_table: dict[tuple[int, int], list[tuple[str, bool]]] | None = None
        self._npc_presence_data: bytes = b""
        self._prev_npc_presence_data: bytes | None = None

        # Booster Hill counter mapping from spoiler ($70B1 threshold checks)
        self._booster_hill_checks: list[tuple[str, int]] | None = None  # (display_name, threshold)
        self._booster_hill_counter: int = 0
        self._prev_booster_hill_counter: int | None = None

    # -----------------------------------------------------------------
    # Public API: connection
    # -----------------------------------------------------------------

    async def connect(self) -> bool:
        """Find SNI device and verify hook is alive."""
        if not await self._reader.connect():
            return False
        return await self.check_hook_alive()

    async def check_hook_alive(self) -> bool:
        """Verify NMI hook is running by checking version + frame counter delta."""
        outbox = self._reader.read_fxpak(MAILBOX_FXPAK_BASE, 0x0F)
        if outbox is None or len(outbox) < 0x0F:
            return False

        version = outbox[OUTBOX_VERSION]
        if version != HOOK_VERSION:
            return False

        frame1 = int.from_bytes(outbox[OUTBOX_FRAME_CTR:OUTBOX_FRAME_CTR + 2], "little")
        await asyncio.sleep(0.1)
        outbox2 = self._reader.read_fxpak(MAILBOX_FXPAK_BASE, 0x0F)
        if outbox2 is None or len(outbox2) < 0x0F:
            return False
        frame2 = int.from_bytes(outbox2[OUTBOX_FRAME_CTR:OUTBOX_FRAME_CTR + 2], "little")

        return frame2 != frame1

    # -----------------------------------------------------------------
    # Public API: check detection
    # -----------------------------------------------------------------

    def on_check(self, callback: Callable[[CheckEvent], None]) -> None:
        """Register a callback for when a new check is detected."""
        self._check_callbacks.append(callback)

    def on_var_change(self, callback: Callable[[VarEvent], None]) -> None:
        """Register a callback for when a non-check flag variable changes."""
        self._var_callbacks.append(callback)

    def on_room_change(self, callback: Callable[[RoomEvent], None]) -> None:
        """Register a callback for when the player enters a new room."""
        self._room_callbacks.append(callback)

    def on_command(self, callback: Callable[[CommandEvent], None]) -> None:
        """Register a callback for when a command is sent to the SNES."""
        self._command_callbacks.append(callback)

    def on_game_mode_change(self, callback: Callable[[GameModeEvent], None]) -> None:
        """Register a callback for when the game mode changes."""
        self._game_mode_callbacks.append(callback)

    def on_currency_change(self, callback: Callable[[CurrencyChangeEvent], None]) -> None:
        """Register a callback for when coins or frog coins change."""
        self._currency_callbacks.append(callback)

    def on_fp_change(self, callback: Callable[[FpChangeEvent], None]) -> None:
        """Register a callback for when FP changes."""
        self._fp_callbacks.append(callback)

    def on_inventory_change(self, callback: Callable[[InventoryChangeEvent], None]) -> None:
        """Register a callback for when inventory contents change."""
        self._inventory_callbacks.append(callback)

    def on_hp_change(self, callback: Callable[[HpChangeEvent], None]) -> None:
        """Register a callback for when character HP changes in overworld."""
        self._hp_callbacks.append(callback)

    def on_star_piece_change(self, callback: Callable[[StarPieceEvent], None]) -> None:
        """Register a callback for when the star piece count changes."""
        self._star_piece_callbacks.append(callback)

    def load_check_mapping(self, spoiler_path: str) -> None:
        """Load check bit mapping from a spoiler JSON file.

        Builds a chest check table in the same format as AP_CHEST_CHECKS,
        keyed by (byte_offset_from_region_base, bit) → [(display_name, set_when_checked)].
        """
        import json
        with open(spoiler_path) as f:
            data = json.load(f)
        cbm = data.get("check_bit_mapping", {})
        if not cbm:
            return
        table: dict[tuple[int, int], list[tuple[str, bool]]] = {}
        for class_name, entry in cbm.items():
            addr = int(entry["addr"], 16)
            byte_off = addr - AP_REGION_CHEST_ADDR
            bit = entry["bit"]
            swc = entry["set_when_checked"]
            display = _format_class_name(class_name)
            table.setdefault((byte_off, bit), []).append((display, swc))
        self._chest_check_table = table

        # Load NPC presence mapping (same format, different base address)
        NPC_PRESENCE_BASE = 0xE02D20
        npm = data.get("npc_presence_mapping", {})
        if npm:
            npc_table: dict[tuple[int, int], list[tuple[str, bool]]] = {}
            for class_name, entry in npm.items():
                addr = int(entry["addr"], 16)
                byte_off = addr - NPC_PRESENCE_BASE
                bit = entry["bit"]
                swc = entry["set_when_checked"]
                display = _format_class_name(class_name)
                npc_table.setdefault((byte_off, bit), []).append((display, swc))
            self._npc_presence_check_table = npc_table

        # Load Booster Hill counter mapping (threshold-based checks)
        bhm = data.get("booster_hill_mapping", {})
        if bhm:
            hill_checks: list[tuple[str, int]] = []
            for class_name, entry in bhm.items():
                display = _format_class_name(class_name)
                hill_checks.append((display, entry["threshold"]))
            # Sort by threshold so we can fire in order
            hill_checks.sort(key=lambda x: x[1])
            self._booster_hill_checks = hill_checks

    @property
    def checks(self) -> dict[str, bool]:
        """All check keys → completed status."""
        return dict(self._checks)

    # -----------------------------------------------------------------
    # Public API: game state properties
    # -----------------------------------------------------------------

    @property
    def game_mode(self) -> GameMode:
        try:
            return GameMode(self._game_mode_byte)
        except ValueError:
            return GameMode.UNKNOWN

    @property
    def game_mode_byte(self) -> int:
        """Raw game mode byte for modes not in the enum."""
        return self._game_mode_byte

    @property
    def in_battle(self) -> bool:
        return self._battle_byte != 0

    @property
    def hook_alive(self) -> bool:
        return self._version_byte == HOOK_VERSION

    @property
    def characters(self) -> list[dict[str, int | str]]:
        """Character HP from state dump (full stats not available via FxPak)."""
        result = []
        for i in range(5):
            name = CHARACTER_NAMES.get(i, f"Char {i}")
            result.append({
                "name": name,
                "current_hp": self._cur_hp[i],
                "max_hp": self._max_hp[i],
            })
        return result

    @property
    def party(self) -> list[str]:
        """Current party members from NMI hook outbox (IRAM copies)."""
        if not self._party_slot_data:
            return []
        names = []
        for b in self._party_slot_data:
            if b != 0xFF and b in _RECRUIT_CHARS:
                names.append(_RECRUIT_CHARS[b])
        return names

    @property
    def coins(self) -> int:
        return self._coins

    @property
    def frog_coins(self) -> int:
        return self._frog_coins

    @property
    def current_area(self) -> str:
        """Current area name from NMI hook outbox (IRAM copy)."""
        name = ROOM_NAMES.get(self._area_id, "Unknown")
        return f"[{self._area_id}] {name}"

    @property
    def current_area_id(self) -> int:
        return self._area_id

    @property
    def hidden_chests(self) -> int:
        return self._hidden_chests

    @property
    def boss_victories(self) -> int:
        return self._boss_victories

    @property
    def music_track(self) -> int:
        return self._music_byte

    @property
    def frame_counter(self) -> int:
        return self._frame_counter

    @property
    def star_pieces(self) -> int:
        return self._star_pieces

    @property
    def consumable_count(self) -> int:
        return len(self._consumables)

    @property
    def equipment_count(self) -> int:
        return len(self._equipment)

    @property
    def key_item_count(self) -> int:
        return len(self._key_items)

    @property
    def current_fp(self) -> int:
        return self._current_fp

    @property
    def max_fp(self) -> int:
        return self._max_fp

    # -----------------------------------------------------------------
    # Public API: polling
    # -----------------------------------------------------------------

    # NPC object presence region (BW-RAM $6D20-$6F1F, 512 bytes)
    # Tracks which NPCs are present/removed per level via persistent bits.
    BWRAM_NPC_PRESENCE = (_snes_to_fxpak_bwram(0x6D20), 0x200)

    async def debug_poll(self) -> None:
        """Single read cycle with raw debug output."""
        reads: list[tuple[int, int, int]] = [
            (MAILBOX_FXPAK_BASE, 0x0F, FX),
            (BWRAM_LOWER[0], BWRAM_LOWER[1], FX),
            (BWRAM_EVENT_FLAGS[0], BWRAM_EVENT_FLAGS[1], FX),
            (BWRAM_CHESTS[0], BWRAM_CHESTS[1], FX),
            (BWRAM_HIDDEN_CHESTS[0], BWRAM_HIDDEN_CHESTS[1], FX),
            (BWRAM_BOSS_VICTORIES[0], BWRAM_BOSS_VICTORIES[1], FX),
            (BWRAM_MENU_FLAGS[0], BWRAM_MENU_FLAGS[1], FX),
            # Star pieces — index 7
            (0xE030D5, 1, FX),
            # NPC presence — index 8
            (self.BWRAM_NPC_PRESENCE[0], self.BWRAM_NPC_PRESENCE[1], FX),
        ]
        labels = [
            "mailbox_outbox", "lower_bwram", "event_flags", "chests",
            "hidden_chests", "boss_victories", "menu_flags", "star_pieces",
            "npc_presence",
        ]
        results = self._reader.multi_read(reads)
        for i, (label, result) in enumerate(zip(labels, results)):
            addr, size, _ = reads[i]
            if result is None:
                print(f"  [{i}] {label} @ 0x{addr:06X}: FAILED (None)")
            else:
                hex_str = result[:16].hex(" ")
                suffix = "..." if len(result) > 16 else ""
                print(f"  [{i}] {label} @ 0x{addr:06X}: {len(result)}B = {hex_str}{suffix}")

    def read_npc_presence(self) -> bytes | None:
        """Read the full 512-byte NPC presence region from BW-RAM."""
        return self._reader.read_fxpak(
            self.BWRAM_NPC_PRESENCE[0], self.BWRAM_NPC_PRESENCE[1],
        )

    async def poll(self) -> None:
        """Single read cycle: read all state, fire check callbacks for changes.

        All reads use FxPakPro address space (SRAM for BW-RAM, SRAM for mailbox).
        WRAM data (coins, characters) comes from periodic CMD_STATE_DUMP.
        """
        # All reads go through FxPakPro — no SnesABus (broken on SA-1 hardware)
        reads: list[tuple[int, int, int]] = [
            # Mailbox outbox (FxPakPro SRAM $E03F00) — index 0
            # 15 bytes: music(1)+battle(1)+frame(2)+ver(1)+result(1)+mode(1)+area(2)+party(5)+count(1)
            (MAILBOX_FXPAK_BASE, 0x0F, FX),
            # Lower BW-RAM (key items, NPC triggers) — index 1
            (BWRAM_LOWER[0], BWRAM_LOWER[1], FX),
            # Event flags (BW-RAM via FxPakPro SRAM) — index 2
            (BWRAM_EVENT_FLAGS[0], BWRAM_EVENT_FLAGS[1], FX),
            # Treasure chests — index 3
            (BWRAM_CHESTS[0], BWRAM_CHESTS[1], FX),
            # Hidden chests — index 4
            (BWRAM_HIDDEN_CHESTS[0], BWRAM_HIDDEN_CHESTS[1], FX),
            # Boss victories — index 5
            (BWRAM_BOSS_VICTORIES[0], BWRAM_BOSS_VICTORIES[1], FX),
            # Menu flags — index 6
            (BWRAM_MENU_FLAGS[0], BWRAM_MENU_FLAGS[1], FX),
            # Star pieces — index 7
            (0xE030D5, 1, FX),
            # NPC presence — index 8
            (self.BWRAM_NPC_PRESENCE[0], self.BWRAM_NPC_PRESENCE[1], FX),
            # Booster Hill flower counter — index 9
            (BWRAM_BOOSTER_HILL_CTR[0], BWRAM_BOOSTER_HILL_CTR[1], FX),
        ]

        results = self._reader.multi_read(reads)

        # Parse mailbox outbox (15 bytes)
        outbox = results[0]
        if isinstance(outbox, bytes) and len(outbox) >= 0x0F:
            self._music_byte = outbox[OUTBOX_MUSIC]
            self._battle_byte = outbox[OUTBOX_BATTLE]
            self._frame_counter = int.from_bytes(
                outbox[OUTBOX_FRAME_CTR:OUTBOX_FRAME_CTR + 2], "little"
            )
            self._version_byte = outbox[OUTBOX_VERSION]
            self._result_byte = outbox[OUTBOX_RESULT]
            self._game_mode_byte = outbox[OUTBOX_GAME_MODE]

            # Game mode change detection
            if (
                self._prev_game_mode_byte is not None
                and self._game_mode_byte != self._prev_game_mode_byte
                and not self._first_poll
            ):
                try:
                    old_mode = GameMode(self._prev_game_mode_byte)
                except ValueError:
                    old_mode = GameMode.UNKNOWN
                try:
                    new_mode = GameMode(self._game_mode_byte)
                except ValueError:
                    new_mode = GameMode.UNKNOWN
                self._fire_game_mode(GameModeEvent(
                    old_mode, self._prev_game_mode_byte,
                    new_mode, self._game_mode_byte, time.time(),
                ))
            self._prev_game_mode_byte = self._game_mode_byte

            new_area_id = int.from_bytes(
                outbox[OUTBOX_AREA_ID:OUTBOX_AREA_ID + 2], "little"
            )
            if (
                self._prev_area_id is not None
                and new_area_id != self._prev_area_id
                and not self._first_poll
            ):
                now = time.time()
                self._fire_room(RoomEvent(
                    room_id=new_area_id,
                    room_name=ROOM_NAMES.get(new_area_id, "Unknown"),
                    prev_room_id=self._prev_area_id,
                    prev_room_name=ROOM_NAMES.get(self._prev_area_id, "Unknown"),
                    timestamp=now,
                ))
            self._prev_area_id = new_area_id
            self._area_id = new_area_id
            self._party_slot_data = outbox[OUTBOX_PARTY_SLOTS:OUTBOX_PARTY_SLOTS + 5]
            self._party_count = outbox[OUTBOX_PARTY_COUNT]

        # Parse BW-RAM data (via FxPakPro SRAM)
        lower_data = results[1]
        if isinstance(lower_data, bytes):
            self._lower_data = lower_data

        event_data = results[2]
        if isinstance(event_data, bytes):
            self._event_data = event_data

        chest_data = results[3]
        if isinstance(chest_data, bytes):
            self._chest_data = chest_data

        hidden = results[4]
        if isinstance(hidden, bytes) and len(hidden) >= 1:
            self._hidden_chests = hidden[0]

        boss_vic = results[5]
        if isinstance(boss_vic, bytes) and len(boss_vic) >= 1:
            self._boss_victories = boss_vic[0]

        menu = results[6]
        if isinstance(menu, bytes) and len(menu) >= 1:
            self._menu_flags = menu[0]

        # Star pieces
        star_data = results[7]
        if isinstance(star_data, bytes) and len(star_data) >= 1:
            self._star_pieces = star_data[0]
            if (
                self._prev_star_pieces is not None
                and self._star_pieces != self._prev_star_pieces
                and not self._first_poll
            ):
                self._fire_star_piece(StarPieceEvent(
                    self._prev_star_pieces, self._star_pieces, time.time(),
                ))
            self._prev_star_pieces = self._star_pieces

        # NPC presence
        npc_pres = results[8]
        if isinstance(npc_pres, bytes):
            self._npc_presence_data = npc_pres

        # Booster Hill flower counter
        hill_data = results[9]
        if isinstance(hill_data, bytes) and len(hill_data) >= 1:
            self._booster_hill_counter = hill_data[0]

        # Periodic state dump for WRAM data (coins, characters, inventory)
        now = time.time()
        if now - self._last_state_dump >= self._state_dump_interval:
            await self._do_state_dump()
            self._last_state_dump = now

        # --- Check detection ---
        # Skip during battles: the battle engine temporarily overwrites BW-RAM
        # event flags, causing false diffs. Defer detection to overworld.
        if self._game_mode_byte not in (
            GameMode.BATTLE_SETUP, 0xC2,  # 0xC2 = in-battle (not in enum)
        ):
            self._detect_checks()

    async def _do_state_dump(self) -> None:
        """Request state dump from hook and parse WRAM data (coins, HP).

        Also diffs against previous dump and fires change events.
        """
        # Send CMD_STATE_DUMP and wait for ack
        ok = await self._send_command(CMD_STATE_DUMP)
        if not ok:
            return

        # Read the dump area from FxPakPro SRAM
        dump = self._reader.read_fxpak(
            MAILBOX_FXPAK_BASE + OUTBOX_CONSUMABLES, 0x74
        )
        if not isinstance(dump, bytes) or len(dump) < 0x74:
            return

        base = OUTBOX_CONSUMABLES
        self._coins = int.from_bytes(
            dump[OUTBOX_COINS - base:OUTBOX_COINS - base + 2], "little"
        )
        self._current_fp = dump[OUTBOX_CURRENT_FP - base]
        self._max_fp = dump[OUTBOX_MAX_FP - base]
        self._frog_coins = int.from_bytes(
            dump[OUTBOX_FROG_COINS - base:OUTBOX_FROG_COINS - base + 2], "little"
        )
        for i in range(5):
            self._cur_hp[i] = int.from_bytes(
                dump[OUTBOX_CUR_HP - base + i * 2:OUTBOX_CUR_HP - base + i * 2 + 2],
                "little",
            )
            self._max_hp[i] = int.from_bytes(
                dump[OUTBOX_MAX_HP - base + i * 2:OUTBOX_MAX_HP - base + i * 2 + 2],
                "little",
            )

        # Parse inventory lists (filter 0xFF empty slots)
        self._consumables = [b for b in dump[0:30] if b != 0xFF]
        self._equipment = [
            b for b in dump[OUTBOX_EQUIPMENT - base:OUTBOX_EQUIPMENT - base + 30]
            if b != 0xFF
        ]
        self._key_items = [
            b for b in dump[OUTBOX_KEY_ITEMS - base:OUTBOX_KEY_ITEMS - base + 30]
            if b != 0xFF
        ]

        # --- Diff against previous state and fire events ---
        now = time.time()

        # Currency diffing
        if self._prev_coins is not None and self._coins != self._prev_coins:
            self._fire_currency(CurrencyChangeEvent(
                "coins", self._prev_coins, self._coins,
                self._coins - self._prev_coins, now,
            ))
        if self._prev_frog_coins is not None and self._frog_coins != self._prev_frog_coins:
            self._fire_currency(CurrencyChangeEvent(
                "frog_coins", self._prev_frog_coins, self._frog_coins,
                self._frog_coins - self._prev_frog_coins, now,
            ))

        # FP diffing
        if self._prev_current_fp is not None and (
            self._current_fp != self._prev_current_fp
            or self._max_fp != self._prev_max_fp
        ):
            self._fire_fp(FpChangeEvent(
                self._prev_current_fp, self._current_fp,
                self._max_fp, self._prev_max_fp if self._prev_max_fp is not None else self._max_fp,
                now,
            ))

        # HP diffing (overworld only to avoid battle noise)
        if self._prev_cur_hp is not None and self.game_mode == GameMode.OVERWORLD:
            for i in range(5):
                if self._cur_hp[i] != self._prev_cur_hp[i] and self._max_hp[i] > 0:
                    self._fire_hp(HpChangeEvent(
                        i, CHARACTER_NAMES.get(i, f"Char {i}"),
                        self._prev_cur_hp[i], self._cur_hp[i],
                        self._max_hp[i], now,
                    ))

        # Inventory diffing
        if self._prev_consumables is not None:
            self._diff_inventory("consumable", self._prev_consumables, self._consumables, now)
        if self._prev_equipment is not None:
            self._diff_inventory("equipment", self._prev_equipment, self._equipment, now)
        if self._prev_key_items is not None:
            self._diff_inventory("key_item", self._prev_key_items, self._key_items, now)

        # Save previous state for next diff
        self._prev_coins = self._coins
        self._prev_frog_coins = self._frog_coins
        self._prev_current_fp = self._current_fp
        self._prev_max_fp = self._max_fp
        self._prev_cur_hp = list(self._cur_hp)
        self._prev_max_hp = list(self._max_hp)
        self._prev_consumables = list(self._consumables)
        self._prev_equipment = list(self._equipment)
        self._prev_key_items = list(self._key_items)

    def _diff_inventory(
        self, inv_type: str, old_list: list[int], new_list: list[int], now: float,
    ) -> None:
        """Diff two inventory lists using Counter and fire InventoryChangeEvent."""
        old_counts = Counter(old_list)
        new_counts = Counter(new_list)
        added = list((new_counts - old_counts).elements())
        removed = list((old_counts - new_counts).elements())
        if added or removed:
            self._fire_inventory(InventoryChangeEvent(
                inv_type, added, removed, len(new_list), now,
            ))

    def _diff_region_checks(
        self,
        current: bytes,
        previous: bytes | None,
        region_size: int,
        check_table: dict[tuple[int, int], list[tuple[str, bool]]],
        now: float,
    ) -> None:
        """Diff a BW-RAM region and fire check events for AP location changes.

        Handles polarity: set_when_checked=True fires on 0→1, False on 1→0.
        """
        if previous is None or self._first_poll:
            return
        scan_len = min(len(current), len(previous), region_size)
        for byte_off in range(scan_len):
            diff = current[byte_off] ^ previous[byte_off]
            if diff == 0:
                continue
            for bit in range(8):
                if not (diff & (1 << bit)):
                    continue
                is_set = bool(current[byte_off] & (1 << bit))
                entries = check_table.get((byte_off, bit))
                if not entries:
                    continue
                for check_name, set_when_checked in entries:
                    # Polarity: fire when transition matches expectation
                    if set_when_checked and is_set:
                        # Bit went 0→1, check expects SET = done
                        pass  # fire below
                    elif not set_when_checked and not is_set:
                        # Bit went 1→0, check expects CLEAR = done
                        pass  # fire below
                    else:
                        continue
                    if not self._checks.get(check_name, False):
                        self._checks[check_name] = True
                        self._fire_check(CheckEvent(
                            _check_type_from_name(check_name),
                            check_name,
                            check_name,
                            now,
                        ))

    def _detect_checks(self) -> None:
        """Diff all BW-RAM regions and party slots, fire callbacks for changes."""
        now = time.time()

        # Lower BW-RAM region (key items, NPC triggers, some bosses)
        if isinstance(self._lower_data, bytes) and len(self._lower_data) > 0:
            self._diff_region_checks(
                self._lower_data, self._prev_lower_data,
                AP_REGION_LOWER_SIZE, AP_LOWER_CHECKS, now,
            )
            self._prev_lower_data = bytes(self._lower_data)

        # Event flag region (96 bytes — bosses, events, key items)
        if isinstance(self._event_data, bytes) and len(self._event_data) > 0:
            self._diff_region_checks(
                self._event_data, self._prev_event_data,
                AP_REGION_EVENT_SIZE, AP_EVENT_CHECKS, now,
            )
            # Also fire VarEvents for named flag changes, and promote to CheckEvents
            # when the variable matches a CHECK_CONDITIONS entry
            if self._prev_event_data is not None and not self._first_poll:
                prev = self._prev_event_data
                scan_len = min(len(self._event_data), len(prev), AP_REGION_EVENT_SIZE)
                for byte_off in range(scan_len):
                    diff = self._event_data[byte_off] ^ prev[byte_off]
                    if diff == 0:
                        continue
                    for bit in range(8):
                        if not (diff & (1 << bit)):
                            continue
                        var_name = FLAG_NAMES.get((byte_off, bit))
                        if not var_name:
                            continue
                        is_set = bool(self._event_data[byte_off] & (1 << bit))
                        # Check if this var being SET completes a simple check condition
                        if is_set and var_name in CHECK_CONDITIONS:
                            for class_name in CHECK_CONDITIONS[var_name]:
                                if not self._checks.get(class_name, False):
                                    self._checks[class_name] = True
                                    self._fire_check(CheckEvent(
                                        CheckType.FLAG,
                                        class_name,
                                        _format_class_name(class_name),
                                        now,
                                    ))
                        else:
                            # Only fire VarEvent if not promoted to a check
                            self._fire_var(VarEvent(
                                var_name, byte_off, bit, is_set, now,
                            ))
                # Check compound conditions (all required vars must be set)
                for class_name, required_vars in COMPOUND_CHECKS:
                    if self._checks.get(class_name, False):
                        continue
                    if all(self._is_flag_set(v) for v in required_vars):
                        self._checks[class_name] = True
                        self._fire_check(CheckEvent(
                            CheckType.FLAG,
                            class_name,
                            _format_class_name(class_name),
                            now,
                        ))
            self._prev_event_data = bytes(self._event_data)

        # Treasure chest region (use spoiler mapping if loaded, else AP fallback)
        chest_table = self._chest_check_table if self._chest_check_table is not None else AP_CHEST_CHECKS
        if isinstance(self._chest_data, bytes) and len(self._chest_data) > 0:
            self._diff_region_checks(
                self._chest_data, self._prev_chest_data,
                AP_REGION_CHEST_SIZE, chest_table, now,
            )
            self._prev_chest_data = bytes(self._chest_data)

        # NPC presence region (use spoiler mapping if loaded)
        if (
            self._npc_presence_check_table is not None
            and isinstance(self._npc_presence_data, bytes)
            and len(self._npc_presence_data) > 0
        ):
            self._diff_region_checks(
                self._npc_presence_data, self._prev_npc_presence_data,
                0x200, self._npc_presence_check_table, now,
            )
            self._prev_npc_presence_data = bytes(self._npc_presence_data)

        # Booster Hill flower counter (threshold-based checks)
        if (
            self._booster_hill_checks is not None
            and self._prev_booster_hill_counter is not None
            and not self._first_poll
            and self._booster_hill_counter != self._prev_booster_hill_counter
        ):
            old_val = self._prev_booster_hill_counter
            new_val = self._booster_hill_counter
            for check_name, threshold in self._booster_hill_checks:
                if old_val < threshold <= new_val:
                    if not self._checks.get(check_name, False):
                        self._checks[check_name] = True
                        self._fire_check(CheckEvent(
                            _check_type_from_name(check_name),
                            check_name,
                            check_name,
                            now,
                        ))
        self._prev_booster_hill_counter = self._booster_hill_counter

        # Recruitment checks via party slot diffs (IRAM copied to outbox by hook)
        if isinstance(self._party_slot_data, bytes) and len(self._party_slot_data) >= 5:
            current_chars = [b for b in self._party_slot_data if b != 0xFF and b in _RECRUIT_CHARS]
            if self._prev_party_chars is not None and not self._first_poll:
                for char_id in current_chars:
                    if char_id not in self._prev_party_chars:
                        char_name = _RECRUIT_CHARS[char_id]
                        key = f"recruited_{char_name.lower()}"
                        if not self._checks.get(key, False):
                            self._checks[key] = True
                            self._fire_check(CheckEvent(
                                CheckType.RECRUITMENT,
                                key,
                                f"{char_name} Recruited",
                                now,
                            ))
            self._prev_party_chars = current_chars

        self._first_poll = False

    def _fire_check(self, event: CheckEvent) -> None:
        """Invoke all registered check callbacks."""
        for cb in self._check_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_var(self, event: VarEvent) -> None:
        """Invoke all registered variable change callbacks."""
        for cb in self._var_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_room(self, event: RoomEvent) -> None:
        """Invoke all registered room change callbacks."""
        for cb in self._room_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_command(self, event: CommandEvent) -> None:
        """Invoke all registered command callbacks."""
        for cb in self._command_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_game_mode(self, event: GameModeEvent) -> None:
        for cb in self._game_mode_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_currency(self, event: CurrencyChangeEvent) -> None:
        for cb in self._currency_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_fp(self, event: FpChangeEvent) -> None:
        for cb in self._fp_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_inventory(self, event: InventoryChangeEvent) -> None:
        for cb in self._inventory_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_hp(self, event: HpChangeEvent) -> None:
        for cb in self._hp_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _fire_star_piece(self, event: StarPieceEvent) -> None:
        for cb in self._star_piece_callbacks:
            try:
                cb(event)
            except Exception:
                pass

    def _is_flag_set(self, var_name: str) -> bool:
        """Check if a named flag variable is currently set in event data."""
        pos = _FLAG_NAME_TO_POS.get(var_name)
        if pos is None:
            return False
        return check_flag(self._event_data, pos[0], pos[1])

    # -----------------------------------------------------------------
    # Public API: main loop
    # -----------------------------------------------------------------

    async def run(self, refresh_ms: int = 200) -> None:
        """Continuous polling loop."""
        while True:
            await self.poll()
            await asyncio.sleep(refresh_ms / 1000.0)

    # -----------------------------------------------------------------
    # Public API: item delivery
    # -----------------------------------------------------------------

    async def give_item(self, item_type: int, item_id: int) -> bool:
        """Give an item via the NMI hook mailbox.

        Args:
            item_type: 0=consumable, 1=equipment, 2=key item
            item_id: Item ID byte
        """
        return await self._send_command(CMD_GIVE_ITEM, item_type, item_id)

    async def add_coins(self, amount: int) -> bool:
        """Add coins (capped at 999 by the hook)."""
        return await self._send_command(
            CMD_ADD_COINS, 0, 0,
            amount.to_bytes(2, "little"),
        )

    async def add_frog_coins(self, amount: int) -> bool:
        """Add frog coins (capped at 999 by the hook)."""
        return await self._send_command(
            CMD_ADD_FROG_COINS, 0, 0,
            amount.to_bytes(2, "little"),
        )

    async def add_star_piece(self) -> bool:
        """Increment star piece counter (capped at 7 by the hook)."""
        return await self._send_command(CMD_ADD_STAR_PIECE)

    async def recruit_character(self, char_id: int) -> bool:
        """Recruit a character (0=Mario, 1=Peach, 2=Bowser, 3=Geno, 4=Mallow)."""
        return await self._send_command(CMD_RECRUIT_CHAR, 0, char_id)

    async def learn_spell(self, char_idx: int, spell_bit: int) -> bool:
        """Teach a spell to a character.

        Args:
            char_idx: Character index 0-4
            spell_bit: Spell bit index 0-31
        """
        return await self._send_command(CMD_LEARN_SPELL, char_idx, spell_bit)

    async def heal(self) -> bool:
        """Heal all characters to full HP and restore FP."""
        return await self._send_command(CMD_HEAL)

    async def set_coins(self, amount: int) -> bool:
        """Set coins to exact amount."""
        return await self._send_command(
            CMD_SET_COINS, 0, 0,
            amount.to_bytes(2, "little"),
        )

    async def set_frog_coins(self, amount: int) -> bool:
        """Set frog coins to exact amount."""
        return await self._send_command(
            CMD_SET_FROG_COINS, 0, 0,
            amount.to_bytes(2, "little"),
        )

    async def request_state_dump(self) -> dict[str, list[int] | int] | None:
        """Request a full state dump from the hook and parse the result.

        Returns dict with keys: consumables, equipment, key_items,
        coins, current_fp, max_fp, frog_coins, cur_hp, max_hp
        """
        ok = await self._send_command(CMD_STATE_DUMP)
        if not ok:
            return None

        # Read the full outbox dump area
        dump = self._reader.read_fxpak(MAILBOX_FXPAK_BASE + OUTBOX_CONSUMABLES, 0x74)
        if dump is None:
            return None

        base = OUTBOX_CONSUMABLES
        return {
            "consumables": [
                b for b in dump[0:30] if b != 0xFF
            ],
            "equipment": [
                b for b in dump[OUTBOX_EQUIPMENT - base:OUTBOX_EQUIPMENT - base + 30]
                if b != 0xFF
            ],
            "key_items": [
                b for b in dump[OUTBOX_KEY_ITEMS - base:OUTBOX_KEY_ITEMS - base + 30]
                if b != 0xFF
            ],
            "coins": int.from_bytes(
                dump[OUTBOX_COINS - base:OUTBOX_COINS - base + 2], "little"
            ),
            "current_fp": dump[OUTBOX_CURRENT_FP - base],
            "max_fp": dump[OUTBOX_MAX_FP - base],
            "frog_coins": int.from_bytes(
                dump[OUTBOX_FROG_COINS - base:OUTBOX_FROG_COINS - base + 2], "little"
            ),
            "cur_hp": [
                int.from_bytes(dump[OUTBOX_CUR_HP - base + i * 2:OUTBOX_CUR_HP - base + i * 2 + 2], "little")
                for i in range(5)
            ],
            "max_hp": [
                int.from_bytes(dump[OUTBOX_MAX_HP - base + i * 2:OUTBOX_MAX_HP - base + i * 2 + 2], "little")
                for i in range(5)
            ],
        }

    # -----------------------------------------------------------------
    # Internal: mailbox command protocol
    # -----------------------------------------------------------------

    _CMD_NAMES: dict[int, str] = {
        CMD_IDLE: "IDLE",
        CMD_GIVE_ITEM: "GIVE_ITEM",
        CMD_SET_COINS: "SET_COINS",
        CMD_SET_FROG_COINS: "SET_FROG_COINS",
        CMD_ADD_COINS: "ADD_COINS",
        CMD_ADD_FROG_COINS: "ADD_FROG_COINS",
        CMD_ADD_STAR_PIECE: "ADD_STAR_PIECE",
        CMD_RECRUIT_CHAR: "RECRUIT_CHAR",
        CMD_LEARN_SPELL: "LEARN_SPELL",
        CMD_STATE_DUMP: "STATE_DUMP",
        CMD_HEAL: "HEAL",
    }

    async def _send_command(
        self,
        cmd: int,
        p1: int = 0,
        p2: int = 0,
        p3_bytes: bytes | None = None,
    ) -> bool:
        """Send a command to the NMI hook mailbox and wait for acknowledgment.

        Protocol: write params first, then command byte. Poll until command
        byte clears (hook sets it to 0 after processing).
        """
        # Write params first
        params = bytes([p1, p2])
        if p3_bytes is not None:
            params += p3_bytes
        else:
            params += bytes([0, 0])

        if not self._reader.write_fxpak(
            MAILBOX_FXPAK_BASE + INBOX_PARAM1, params
        ):
            self._fire_command(CommandEvent(
                cmd, self._CMD_NAMES.get(cmd, f"0x{cmd:02X}"),
                p1, p2, False, time.time(),
            ))
            return False

        # Write command byte (triggers processing)
        if not self._reader.write_fxpak(
            MAILBOX_FXPAK_BASE + INBOX_COMMAND, bytes([cmd])
        ):
            self._fire_command(CommandEvent(
                cmd, self._CMD_NAMES.get(cmd, f"0x{cmd:02X}"),
                p1, p2, False, time.time(),
            ))
            return False

        # Poll for acknowledgment (command byte clears to 0)
        for _ in range(30):  # ~1.5 seconds at 50ms intervals
            await asyncio.sleep(0.05)
            data = self._reader.read_fxpak(MAILBOX_FXPAK_BASE + INBOX_COMMAND, 1)
            if isinstance(data, bytes) and len(data) >= 1 and data[0] == CMD_IDLE:
                # Check result
                result = self._reader.read_fxpak(
                    MAILBOX_FXPAK_BASE + OUTBOX_RESULT, 1
                )
                success = True
                if isinstance(result, bytes) and len(result) >= 1:
                    success = result[0] == RESULT_OK
                self._fire_command(CommandEvent(
                    cmd, self._CMD_NAMES.get(cmd, f"0x{cmd:02X}"),
                    p1, p2, success, time.time(),
                ))
                return success
        self._fire_command(CommandEvent(
            cmd, self._CMD_NAMES.get(cmd, f"0x{cmd:02X}"),
            p1, p2, False, time.time(),
        ))
        return False

    # -----------------------------------------------------------------
    # Public API: summary
    # -----------------------------------------------------------------

    def state_summary(self) -> dict[str, str | int | bool | list[str]]:
        """Return a dict summarizing the current game state."""
        mode = self.game_mode
        mode_str = mode.name if mode != GameMode.UNKNOWN else f"0x{self._game_mode_byte:02X}"
        return {
            "game_mode": mode_str,
            "in_battle": self.in_battle,
            "hook_alive": self.hook_alive,
            "area": self.current_area,
            "area_id": self._area_id,
            "party": self.party,
            "coins": self._coins,
            "frog_coins": self._frog_coins,
            "hidden_chests": self._hidden_chests,
            "boss_victories": self._boss_victories,
            "frame_counter": self._frame_counter,
            "music_track": self._music_byte,
        }
