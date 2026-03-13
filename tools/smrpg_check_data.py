"""Static check/flag/room data parsed from project source files.

Parses variable_names.py, room_names.py, and prizelocations.py at import time
using text regex — no dependency on smrpgpatchbuilder.

Also contains AP location check tables from the Archipelago SMRPG world,
which provide authoritative check detection data for all 229 AP locations
across three BW-RAM regions (lower, event flags, treasure chests).

Exports:
    ROOM_NAMES: dict[int, str]  — room ID → display name (509 entries)
    FLAG_NAMES: dict[tuple[int, int], str]  — (byte_offset, bit) → var name (768 entries)
    CHECK_CONDITIONS: dict[str, list[str]]  — var name → check class names
    COMPOUND_CHECKS: list[tuple[str, list[str]]]  — (class_name, [required_var_names])
    check_flag(data, byte_offset, bit) → bool

    AP check detection:
    AP_REGION_LOWER_ADDR/SIZE — lower BW-RAM region (key items, NPC triggers)
    AP_REGION_EVENT_ADDR/SIZE — event flag region
    AP_REGION_CHEST_ADDR/SIZE — treasure chest region
    AP_LOWER_CHECKS — per-region lookup for lower BW-RAM
    AP_EVENT_CHECKS — per-region lookup for event flags
    AP_CHEST_CHECKS — per-region lookup for treasure chests
"""

from __future__ import annotations

import os
import re

# Paths relative to this file's directory (tools/)
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_THIS_DIR)

_VARIABLE_NAMES_PATH = os.path.join(
    _REPO_ROOT, "randomizer", "data", "variables", "variable_names.py"
)
_ROOM_NAMES_PATH = os.path.join(
    _REPO_ROOT, "randomizer", "data", "variables", "room_names.py"
)
_PRIZE_LOCATIONS_PATH = os.path.join(
    _REPO_ROOT, "randomizer", "progression", "prizelocations.py"
)


def check_flag(data: bytes, byte_offset: int, bit: int) -> bool:
    """Check a single flag bit in event flag data."""
    if byte_offset < len(data):
        return bool(data[byte_offset] & (1 << bit))
    return False


# ---------------------------------------------------------------------------
# Room names
# ---------------------------------------------------------------------------

def _parse_room_names() -> dict[int, str]:
    """Parse room_names.py → {room_id: display_name}.

    Format: R###_DESCRIPTIVE_NAME = ###
    """
    rooms: dict[int, str] = {}
    pattern = re.compile(r"^R\d+_(.+?)\s*=\s*(\d+)")
    with open(_ROOM_NAMES_PATH) as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                raw_name = m.group(1)
                room_id = int(m.group(2))
                # UPPER_SNAKE_CASE → Title Case with spaces
                display = raw_name.replace("_", " ").title()
                rooms[room_id] = display
    return rooms


# ---------------------------------------------------------------------------
# Flag variable names
# ---------------------------------------------------------------------------

def _parse_flag_names() -> dict[tuple[int, int], str]:
    """Parse variable_names.py → {(byte_offset, bit): var_name} for Flag() defs.

    byte_offset is relative to $7040 (0-95), matching the 96-byte event flag read.
    """
    flags: dict[tuple[int, int], str] = {}
    pattern = re.compile(r"^(\w+)\s*=\s*Flag\(0x([0-9A-Fa-f]+),\s*(\d+)\)")
    with open(_VARIABLE_NAMES_PATH) as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                var_name = m.group(1)
                address = int(m.group(2), 16)
                bit = int(m.group(3))
                byte_offset = address - 0x7040
                if 0 <= byte_offset < 96:
                    flags[(byte_offset, bit)] = var_name
    return flags


# ---------------------------------------------------------------------------
# Check conditions from prizelocations.py
# ---------------------------------------------------------------------------

def _parse_check_conditions() -> tuple[dict[str, list[str]], list[tuple[str, list[str]]]]:
    """Parse prizelocations.py → check condition mappings.

    Returns:
        simple: {variable_name: [class_names]} for single-variable checks
        compound: [(class_name, [required_var_names])] for multi-variable checks
    """
    simple: dict[str, list[str]] = {}
    compound: list[tuple[str, list[str]]] = []

    class_pattern = re.compile(r"^class\s+(\w+)")
    # Single variable: "# Flag as checked: VAR_NAME" or "# Flag as checked: VAR_NAME set"
    single_flag = re.compile(r"#\s*Flag as checked:\s+(\w+)", re.IGNORECASE)
    # Compound: "# Flag as checked: VAR1 and VAR2 must BOTH be set"
    compound_flag = re.compile(
        r"#\s*Flag as checked:\s+(\w+)\s+and\s+(\w+)\s+must\s+BOTH", re.IGNORECASE
    )

    current_class = ""
    with open(_PRIZE_LOCATIONS_PATH) as f:
        for line in f:
            stripped = line.strip()

            cm = class_pattern.match(stripped)
            if cm:
                current_class = cm.group(1)
                continue

            if "flag as checked:" not in stripped.lower():
                continue

            # Extract the condition text after the colon
            condition_text = stripped.split("Flag as checked:")[-1].strip()

            # Skip NPC/room-based conditions (not detectable via event flags)
            lower_cond = condition_text.lower()
            if "npc " in lower_cond or "in room" in lower_cond:
                continue

            # Check compound condition first
            comp = compound_flag.search(stripped)
            if comp and current_class:
                compound.append((
                    current_class,
                    [comp.group(1), comp.group(2)],
                ))
                continue

            # Single variable condition
            fm = single_flag.search(stripped)
            if fm and current_class:
                var_name = fm.group(1)
                # "NPC" prefix means it's an NPC description, skip
                if var_name.upper().startswith("NPC"):
                    continue
                simple.setdefault(var_name, [])
                if current_class not in simple[var_name]:
                    simple[var_name].append(current_class)

    return simple, compound


# ---------------------------------------------------------------------------
# Module-level data (parsed once at import)
# ---------------------------------------------------------------------------

ROOM_NAMES: dict[int, str] = _parse_room_names()
FLAG_NAMES: dict[tuple[int, int], str] = _parse_flag_names()
CHECK_CONDITIONS: dict[str, list[str]]
COMPOUND_CHECKS: list[tuple[str, list[str]]]
CHECK_CONDITIONS, COMPOUND_CHECKS = _parse_check_conditions()


# ---------------------------------------------------------------------------
# AP location check data (from Archipelago SMRPG world Rom.py)
# ---------------------------------------------------------------------------
#
# Three BW-RAM read regions cover all 229 AP location checks:
#   Lower:  0xE02D00-0xE02E8F  (key items, NPC triggers, some bosses)
#   Events: 0xE03040-0xE0309F  (event flags — same as existing read)
#   Chests: 0xE03D80-0xE03D98  (treasure chest opened bits)
#
# Each check has a polarity (set_when_checked):
#   True  = bit SET means check is done    (detect 0→1 transition)
#   False = bit CLEARED means check is done (detect 1→0 transition)

AP_REGION_LOWER_ADDR = 0xE02D00
AP_REGION_LOWER_SIZE = 0x190   # 400 bytes, covers 0xE02D00-0xE02E8F
AP_REGION_EVENT_ADDR = 0xE03040
AP_REGION_EVENT_SIZE = 0x60    # 96 bytes
AP_REGION_CHEST_ADDR = 0xE03D80
AP_REGION_CHEST_SIZE = 0x19    # 25 bytes

# Raw AP location data: (name, fxpak_addr, bit_index, set_when_checked)
# Addresses are absolute FxPakPro SRAM addresses.
# base_memory_address = 0xE00000, treasure_chest_base_address = 0xE03D80
_AP_RAW: list[tuple[str, int, int, bool]] = [
    # --- Treasure Chests (all set_when_checked=False) ---
    # Mushroom Way
    ("Chest - Mushroom Way 1", 0xE03D89, 6, False),
    ("Chest - Mushroom Way 2", 0xE03D89, 7, False),
    ("Chest - Mushroom Way 3", 0xE03D8A, 0, False),
    ("Chest - Mushroom Way 4", 0xE03D8A, 1, False),
    # Mushroom Kingdom
    ("Chest - Mushroom Kingdom Vault 1", 0xE03D80, 3, False),
    ("Chest - Mushroom Kingdom Vault 2", 0xE03D80, 5, False),
    ("Chest - Mushroom Kingdom Vault 3", 0xE03D80, 4, False),
    # Bandit's Way
    ("Chest - Bandit's Way Flower Jump", 0xE03D8A, 3, False),
    ("Chest - Bandit's Way Guard Dog", 0xE03D82, 0, False),
    ("Chest - Bandit's Way Invincibility Star", 0xE03D82, 1, False),
    ("Chest - Bandit's Way Dog Jump", 0xE03D82, 2, False),
    ("Chest - Bandit's Way Croco Room", 0xE03D8A, 2, False),
    # Kero Sewers
    ("Chest - Kero Sewers Pandorite Room", 0xE03D81, 6, False),
    ("Chest - Kero Sewers Invincibility Star", 0xE03D81, 5, False),
    ("Key Item - Kero Sewers Key Chest (Cricket Jam)", 0xE03D8F, 5, False),
    # Rose Way / Rose Town
    ("Chest - Rose Way Platform Jump", 0xE03D82, 3, False),
    ("Chest - Rose Town Store 1", 0xE03D83, 1, False),
    ("Chest - Rose Town Store 2", 0xE03D83, 2, False),
    # Lazy Shell
    ("Chest - Lazy Shell 1", 0xE03D93, 7, False),
    ("Chest - Lazy Shell 2", 0xE03D94, 0, False),
    # Forest Maze
    ("Chest - Forest Maze 1", 0xE03D8A, 4, False),
    ("Chest - Forest Maze 2", 0xE03D8A, 5, False),
    ("Chest - Forest Maze Underground 1", 0xE03D8D, 4, False),
    ("Chest - Forest Maze Underground 2", 0xE03D8D, 5, False),
    ("Chest - Forest Maze Underground 3", 0xE03D8D, 3, False),
    ("Chest - Forest Maze Red Essence", 0xE03D8A, 6, False),
    # Pipe Vault
    ("Chest - Pipe Vault Slide 1", 0xE03D86, 0, False),
    ("Chest - Pipe Vault Slide 2", 0xE03D85, 7, False),
    ("Chest - Pipe Vault Slide 3", 0xE03D85, 6, False),
    ("Chest - Pipe Vault Nippers 1", 0xE03D86, 1, False),
    ("Chest - Pipe Vault Nippers 2", 0xE03D86, 2, False),
    # Yo'ster Isle
    ("Chest - Yo'ster Isle", 0xE03D80, 6, False),
    # Moleville Mines
    ("Chest - Moleville Mines Invincibility Star", 0xE03D8F, 1, False),
    ("Chest - Moleville Mines Coins", 0xE03D8F, 0, False),
    ("Chest - Moleville Mines Punchinello 1", 0xE03D8F, 2, False),
    ("Chest - Moleville Mines Punchinello 2", 0xE03D8F, 3, False),
    # Booster Pass
    ("Chest - Booster Pass 1", 0xE03D84, 5, False),
    ("Chest - Booster Pass 2", 0xE03D84, 6, False),
    ("Chest - Booster Pass Secret 1", 0xE03D93, 2, False),
    ("Chest - Booster Pass Secret 2", 0xE03D93, 3, False),
    ("Chest - Booster Pass Secret 3", 0xE03D93, 4, False),
    # Booster Tower
    ("Chest - Booster Tower Spookum", 0xE03D89, 0, False),
    ("Chest - Booster Tower Thwomp", 0xE03D81, 0, False),
    ("Chest - Booster Tower Masher", 0xE03D89, 1, False),
    ("Chest - Booster Tower Parachute", 0xE03D80, 7, False),
    ("Chest - Booster Tower Zoom Shoes", 0xE03D81, 1, False),
    ("Chest - Booster Tower Top 1", 0xE03D89, 5, False),
    ("Chest - Booster Tower Top 2", 0xE03D89, 2, False),
    ("Chest - Booster Tower Top 3", 0xE03D89, 4, False),
    # Marrymore
    ("Chest - Marrymore Inn Second Floor", 0xE03D80, 0, False),
    # Sea
    ("Chest - Sea Invincibility Star", 0xE03D86, 7, False),
    ("Chest - Sea Save Room 1", 0xE03D86, 3, False),
    ("Chest - Sea Save Room 2", 0xE03D86, 4, False),
    ("Chest - Sea Save Room 3", 0xE03D86, 5, False),
    ("Chest - Sea Save Room 4", 0xE03D86, 6, False),
    # Sunken Ship
    ("Chest - Sunken Ship Rat Stairs", 0xE03D87, 7, False),
    ("Chest - Sunken Ship Shop", 0xE03D88, 0, False),
    ("Chest - Sunken Ship Coins 1", 0xE03D88, 1, False),
    ("Chest - Sunken Ship Coins 2", 0xE03D88, 2, False),
    ("Chest - Sunken Ship Clone Room", 0xE03D88, 3, False),
    ("Chest - Sunken Ship Frog Coin Room", 0xE03D88, 4, False),
    ("Chest - Sunken Ship Hidon Mushroom", 0xE03D88, 5, False),
    ("Chest - Sunken Ship Safety Ring", 0xE03D88, 7, False),
    ("Chest - Sunken Ship Bandana Reds", 0xE03D80, 2, False),
    # Land's End
    ("Chest - Land's End Red Essence", 0xE03D87, 0, False),
    ("Chest - Land's End Chow Pit 1", 0xE03D87, 1, False),
    ("Chest - Land's End Chow Pit 2", 0xE03D87, 2, False),
    ("Chest - Land's End Bee Room", 0xE03D87, 3, False),
    ("Chest - Land's End Secret 1", 0xE03D8E, 7, False),
    ("Chest - Land's End Secret 2", 0xE03D8E, 6, False),
    ("Chest - Land's End Shy Away", 0xE03D93, 1, False),
    ("Chest - Land's End Invincibility Star 1", 0xE03D8E, 3, False),
    ("Chest - Land's End Invincibility Star 2", 0xE03D8E, 1, False),
    ("Chest - Land's End Invincibility Star 3", 0xE03D8E, 2, False),
    # Belome Temple
    ("Chest - Belome Temple Fortune Teller", 0xE03D94, 1, False),
    ("Chest - Belome Temple After Fortune 1", 0xE03D94, 2, False),
    ("Chest - Belome Temple After Fortune 2", 0xE03D94, 3, False),
    ("Chest - Belome Temple After Fortune 3", 0xE03D94, 5, False),
    ("Chest - Belome Temple After Fortune 4", 0xE03D94, 4, False),
    # Monstro Town
    ("Chest - Monstro Town Entrance", 0xE03D8E, 5, False),
    # Bean Valley
    ("Chest - Bean Valley 1", 0xE03D8E, 0, False),
    ("Chest - Bean Valley 2", 0xE03D8D, 7, False),
    ("Chest - Bean Valley Box Boy Room", 0xE03D91, 1, False),
    ("Chest - Bean Valley Slot Room", 0xE03D91, 3, False),
    ("Chest - Bean Valley Piranha Plants", 0xE03D8D, 6, False),
    ("Chest - Bean Valley Beanstalk", 0xE03D92, 5, False),
    ("Chest - Bean Valley Cloud 1", 0xE03D92, 1, False),
    ("Chest - Bean Valley Cloud 2", 0xE03D92, 2, False),
    ("Chest - Bean Valley Fall 1", 0xE03D92, 3, False),
    ("Chest - Bean Valley Fall 2", 0xE03D92, 4, False),
    # Nimbus Land / Castle
    ("Chest - Nimbus Land Shop", 0xE03D91, 2, False),
    ("Chest - Nimbus Castle Before Birdo 1", 0xE03D84, 7, False),
    ("Chest - Nimbus Castle Before Birdo 2", 0xE03D85, 1, False),
    ("Chest - Nimbus Castle Out Of Bounds 1", 0xE03D93, 5, False),
    ("Chest - Nimbus Castle Out Of Bounds 2", 0xE03D93, 6, False),
    ("Chest - Nimbus Castle Single Gold Bird", 0xE03D85, 0, False),
    ("Chest - Nimbus Castle Invincibility Star", 0xE03D85, 4, False),
    ("Chest - Nimbus Castle Star After Valentina", 0xE03D85, 5, False),
    # Barrel Volcano
    ("Chest - Barrel Volcano Secret 1", 0xE03D91, 6, False),
    ("Chest - Barrel Volcano Secret 2", 0xE03D92, 7, False),
    ("Chest - Barrel Volcano Before Star 1", 0xE03D8F, 5, False),
    ("Chest - Barrel Volcano Before Star 2", 0xE03D92, 7, False),
    ("Chest - Barrel Volcano Invincibility Star", 0xE03D93, 0, False),
    ("Chest - Barrel Volcano Save Room 1", 0xE03D91, 6, False),
    ("Chest - Barrel Volcano Save Room 2", 0xE03D91, 7, False),
    ("Chest - Barrel Volcano Hinopio", 0xE03D92, 0, False),
    # Bowser's Keep
    ("Chest - Bowser's Keep Dark Room", 0xE03D96, 2, False),
    ("Chest - Bowser's Keep Croco Shop 1", 0xE03D80, 0, False),
    ("Chest - Bowser's Keep Croco Shop 2", 0xE03D80, 0, False),
    ("Chest - Bowser's Keep Invisible Bridge 1", 0xE03D8F, 7, False),
    ("Chest - Bowser's Keep Invisible Bridge 2", 0xE03D90, 0, False),
    ("Chest - Bowser's Keep Invisible Bridge 3", 0xE03D90, 1, False),
    ("Chest - Bowser's Keep Invisible Bridge 4", 0xE03D90, 2, False),
    ("Chest - Bowser's Keep Moving Platforms 1", 0xE03D97, 7, False),
    ("Chest - Bowser's Keep Moving Platforms 2", 0xE03D98, 0, False),
    ("Chest - Bowser's Keep Moving Platforms 3", 0xE03D98, 1, False),
    ("Chest - Bowser's Keep Moving Platforms 4", 0xE03D97, 6, False),
    ("Chest - Bowser's Keep Rotating Platforms 1", 0xE03D96, 3, False),
    ("Chest - Bowser's Keep Rotating Platforms 2", 0xE03D96, 6, False),
    ("Chest - Bowser's Keep Rotating Platforms 3", 0xE03D96, 4, False),
    ("Chest - Bowser's Keep Rotating Platforms 4", 0xE03D96, 7, False),
    ("Chest - Bowser's Keep Rotating Platforms 5", 0xE03D96, 5, False),
    ("Chest - Bowser's Keep Rotating Platforms 6", 0xE03D97, 0, False),
    ("Chest - Bowser's Keep Door Reward 1", 0xE03D80, 0, False),
    ("Chest - Bowser's Keep Door Reward 2", 0xE03D87, 4, False),
    ("Chest - Bowser's Keep Door Reward 3", 0xE03D95, 7, False),
    ("Chest - Bowser's Keep Door Reward 4", 0xE03D80, 0, False),
    ("Chest - Bowser's Keep Door Reward 5", 0xE03D80, 0, False),
    ("Chest - Bowser's Keep Door Reward 6", 0xE03D80, 0, False),
    # Factory
    ("Chest - Factory Save Room", 0xE03D8D, 1, False),
    ("Chest - Factory Bolt Platforms", 0xE03D8D, 2, False),
    ("Chest - Factory Falling Axems", 0xE03D80, 0, False),
    ("Chest - Factory Treasure Pit 1", 0xE03D95, 5, False),
    ("Chest - Factory Treasure Pit 2", 0xE03D95, 3, False),
    ("Chest - Factory Conveyor Platforms 1", 0xE03D98, 2, False),
    ("Chest - Factory Conveyor Platforms 2", 0xE03D98, 3, False),
    ("Chest - Factory Behind Snakes 1", 0xE03D95, 4, False),
    ("Chest - Factory Behind Snakes 2", 0xE03D95, 6, False),

    # --- Key Items ---
    ("Key Item - Mario's Bed (Dry Bones Flag)", 0xE02DC0, 4, False),
    ("Key Item - Croco 1 (Rare Frog Coin)", 0xE0304D, 3, True),
    ("Key Item - Rare Frog Coin Reward (Cricket Pie)", 0xE03083, 4, True),
    ("Key Item - Melody Bay Song 1 (Alto Card)", 0xE03051, 4, True),
    ("Key Item - Melody Bay Song 2 (Tenor Card)", 0xE03054, 5, True),
    ("Key Item - Melody Bay Song 3 (Soprano Card)", 0xE03054, 6, True),
    ("Key Item - Rose Town Sign (Greaper Flag)", 0xE02D68, 2, False),
    ("Key Item - Yo'ster Isle Goal (Big Boo Flag)", 0xE02D3A, 0, False),
    ("Key Item - Croco 2 (Bambino Bomb)", 0xE03056, 5, True),
    ("Key Item - Booster Tower Genealogy Hall (Elder Key)", 0xE03054, 0, True),
    ("Key Item - Booster Tower Checkerboard Room (Room Key)", 0xE02DCB, 7, False),
    ("Key Item - Knife Guy (Bright Card)", 0xE03099, 6, True),
    ("Key Item - Seaside Town Key (Shed Key)", 0xE02E19, 3, False),
    ("Key Item - Monstro Town Key (Temple Key)", 0xE02E1F, 6, False),
    ("Key Item - Smilax (Seed)", 0xE02DF6, 1, True),
    ("Key Item - Nimbus Land Guard (Castle Key 1)", 0xE0305F, 6, True),
    ("Key Item - Birdo (Castle Key 2)", 0xE0305F, 5, True),
    ("Key Item - Shy Away (Fertilizer)", 0xE02E6F, 5, False),

    # --- Events ---
    ("Event - Toad Rescue 1", 0xE03052, 4, True),
    ("Event - Toad Rescue 2", 0xE03052, 5, True),
    ("Event - Hammer Bros Reward", 0xE03052, 6, True),
    ("Event - Wallet Guy 1", 0xE03083, 2, True),
    ("Event - Wallet Guy 2", 0xE03083, 2, True),
    ("Event - Mushroom Kingdom Store", 0xE03089, 6, True),
    ("Event - Peach Surprise", 0xE03084, 4, True),
    ("Event - Invasion Family", 0xE03082, 7, True),
    ("Event - Invasion Guest Room", 0xE03083, 0, True),
    ("Event - Invasion Guard", 0xE03082, 5, True),
    ("Event - Croco 1 Reward", 0xE0304D, 5, True),
    ("Event - Pandorite Reward", 0xE03057, 5, True),
    ("Event - Midas River First Time", 0xE03043, 1, True),
    ("Event - Rose Town Toad", 0xE03084, 0, True),
    ("Event - Gaz", 0xE03085, 7, True),
    ("Event - Treasure Seller 1", 0xE03088, 1, True),
    ("Event - Treasure Seller 2", 0xE03088, 0, True),
    ("Event - Treasure Seller 3", 0xE03088, 2, True),
    ("Event - Croco Flunkie 1", 0xE03057, 0, True),
    ("Event - Croco Flunkie 2", 0xE03056, 7, True),
    ("Event - Croco Flunkie 3", 0xE03056, 6, True),
    ("Event - Booster Tower Railway", 0xE02DC6, 0, False),
    ("Event - Booster Tower Chomp", 0xE02DCB, 7, False),
    ("Event - Booster Tower Curtain Game", 0xE03053, 5, True),
    ("Event - Seaside Town Rescue", 0xE03086, 6, True),
    ("Event - Sunken Ship 3D Maze", 0xE0307D, 2, True),
    ("Event - Sunken Ship Cannonball Puzzle", 0xE0307D, 4, True),
    ("Event - Sunken Ship Hidon Reward", 0xE03057, 7, True),
    ("Event - Belome Temple Treasure 1", 0xE02E67, 5, False),
    ("Event - Belome Temple Treasure 2", 0xE02E67, 6, False),
    ("Event - Belome Temple Treasure 3", 0xE02E67, 7, False),
    ("Event - Jinx Dojo Reward", 0xE0308A, 5, True),
    ("Event - Culex Reward", 0xE03093, 4, True),
    ("Event - Super Jumps 30", 0xE03092, 0, True),
    ("Event - Super Jumps 100", 0xE03092, 2, True),
    ("Event - Three Musty Fears", 0xE03089, 7, True),
    ("Event - Troopa Climb", 0xE03094, 7, True),
    ("Event - Dodo Reward", 0xE03093, 1, True),
    ("Event - Nimbus Land Inn", 0xE03098, 6, True),
    ("Event - Nimbus Land Prisoners", 0xE0305F, 7, True),
    ("Event - Nimbus Land Signal Ring", 0xE03084, 3, True),
    ("Event - Nimbus Land Cellar", 0xE0309F, 3, True),
    ("Event - Factory Toad Gift", 0xE03059, 5, True),
    ("Event - Goomba Thumping 1", 0xE03099, 4, True),
    ("Event - Goomba Thumping 2", 0xE03099, 5, True),
    ("Event - Cricket Pie Reward", 0xE03051, 2, True),
    ("Event - Cricket Jam Reward", 0xE03051, 3, False),

    # --- Bosses ---
    ("Boss - Hammer Bros Spot", 0xE03052, 6, True),
    ("Boss - Croco 1 Spot", 0xE0304D, 3, True),
    ("Boss - Mack Spot", 0xE03082, 0, True),
    ("Boss - Pandorite Spot", 0xE03057, 5, True),
    ("Boss - Belome 1 Spot", 0xE03055, 2, True),
    ("Boss - Bowyer Spot", 0xE03083, 6, True),
    ("Boss - Croco 2 Spot", 0xE03056, 5, True),
    ("Boss - Punchinello Spot", 0xE03056, 3, True),
    ("Boss - Booster Spot", 0xE03053, 4, True),
    ("Boss - Knife Guy and Crate Guy Spot", 0xE03048, 6, True),
    ("Boss - Bundt Spot", 0xE0304C, 6, True),
    ("Event - Star Hill Spot", 0xE02DAC, 7, True),
    ("Boss - King Calamari Spot", 0xE03058, 6, True),
    ("Boss - Hidon Spot", 0xE03057, 7, True),
    ("Boss - Johnny Spot", 0xE03058, 7, True),
    ("Boss - Yaridovich Spot", 0xE03086, 0, True),
    ("Boss - Belome 2 Spot", 0xE0307C, 5, True),
    ("Boss - Jagger Spot", 0xE0308A, 2, True),
    ("Boss - Jinx 3 Spot", 0xE0308A, 5, True),
    ("Boss - Culex Spot", 0xE03093, 4, True),
    ("Boss - Box Boy Spot", 0xE03064, 6, True),
    ("Boss - Mega Smilax Spot", 0xE0308C, 3, True),
    ("Boss - Dodo Spot", 0xE03092, 7, True),
    ("Boss - Birdo Spot", 0xE0305F, 5, True),
    ("Boss - Valentina Spot", 0xE0304A, 2, True),
    ("Boss - Czar Dragon Spot", 0xE0307E, 0, True),
    ("Boss - Axem Rangers Spot", 0xE0307D, 7, True),
    ("Boss - Magikoopa Spot", 0xE03093, 6, True),
    ("Boss - Boomer Spot", 0xE03054, 2, True),
    ("Boss - Exor Spot", 0xE03093, 7, True),
    ("Boss - Countdown Spot", 0xE0308F, 7, True),
    ("Boss - Cloaker and Domino Spot", 0xE03096, 0, True),
    ("Boss - Clerk Spot", 0xE03059, 4, True),
    ("Boss - Manager Spot", 0xE03091, 3, True),
    ("Boss - Director Spot", 0xE02E8E, 5, False),
    ("Boss - Gunyolk Spot", 0xE0308F, 6, True),
    ("Boss - Smithy Spot", 0xE0304A, 2, True),
]


def _build_region_checks(
    raw: list[tuple[str, int, int, bool]],
    region_addr: int,
    region_size: int,
) -> dict[tuple[int, int], list[tuple[str, bool]]]:
    """Build per-region lookup: (byte_offset, bit) → [(name, set_when_checked)]."""
    result: dict[tuple[int, int], list[tuple[str, bool]]] = {}
    for name, addr, bit, swc in raw:
        offset = addr - region_addr
        if 0 <= offset < region_size:
            result.setdefault((offset, bit), []).append((name, swc))
    return result


AP_LOWER_CHECKS: dict[tuple[int, int], list[tuple[str, bool]]] = _build_region_checks(
    _AP_RAW, AP_REGION_LOWER_ADDR, AP_REGION_LOWER_SIZE,
)
AP_EVENT_CHECKS: dict[tuple[int, int], list[tuple[str, bool]]] = _build_region_checks(
    _AP_RAW, AP_REGION_EVENT_ADDR, AP_REGION_EVENT_SIZE,
)
AP_CHEST_CHECKS: dict[tuple[int, int], list[tuple[str, bool]]] = _build_region_checks(
    _AP_RAW, AP_REGION_CHEST_ADDR, AP_REGION_CHEST_SIZE,
)
