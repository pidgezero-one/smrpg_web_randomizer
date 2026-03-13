"""
SMRPG Memory Map - Shared definitions for SNI-based tools.

Defines SNES memory addresses, event flags, area names, and character data
structures used by both the debug monitor and auto-tracker.

Address spaces:
  - FxPakPro WRAM: $F50000-$F6FFFF maps to SNES $7E0000-$7FFFFF
  - FxPakPro ROM:  $000000-$DFFFFF maps to SNES ROM linearly
  - FxPakPro SRAM: $E00000-$EFFFFF maps to SNES SRAM
  - SnesABus:      Uses SNES native addressing (bank:offset)

For SA-1 games like SMRPG:
  - BW-RAM at $00:6000-$7FFF (SA-1 side) / $40:0000-$FFFF (SNES side)
  - IRAM at $00:3000-$37FF (SA-1 internal RAM)
  - WRAM at $7E:0000-$7F:FFFF (standard SNES work RAM)
"""

from enum import Enum
from snirk.types import AddressEnum


# =============================================================================
# FxPakPro Address Space - WRAM reads (guaranteed to work)
# SNES $7Exxxx -> FxPakPro $F5xxxx, SNES $7Fxxxx -> FxPakPro $F6xxxx
# =============================================================================

class WRAMAddresses(AddressEnum):
    """WRAM addresses in FxPakPro address space. These are always readable."""

    # --- Character overworld stats ($7F:F800-$7F:F8C0) ---
    # 5 characters x 0x25 bytes each = 0xB9 bytes
    # Char order: Mario(0), Peach(1), Bowser(2), Geno(3), Mallow(4)
    CHARACTER_BLOCK = (0xF6F800, 0xB9)

    # --- Individual character stat blocks (each 0x25 bytes) ---
    MARIO_STATS  = (0xF6F800, 0x25)
    PEACH_STATS  = (0xF6F825, 0x25)
    BOWSER_STATS = (0xF6F84A, 0x25)
    GENO_STATS   = (0xF6F86F, 0x25)
    MALLOW_STATS = (0xF6F894, 0x25)

    # --- Inventory, coins, FP ---
    COINS     = (0xF6F8B9, 0x02)  # $7F:F8B9 - 2 bytes, little-endian
    FROG_COINS = (0xF6F8BB, 0x02)  # $7F:F8BB

    # --- Learned special abilities (randomizer custom) ---
    # $7F:F810 - 5 chars x $14 bytes = $64 bytes
    LEARNED_SPELLS = (0xF6F810, 0x64)

    # --- Battle stats ($7E:FA00-$7E:FFFF) ---
    BATTLE_STATS = (0xF5FA00, 0x0600)

    # --- Battle formation ---
    BATTLE_FORMATION = (0xF50048, 0x02)  # $7E:0048

    # --- World map location ---
    MAP_LOCATION = (0xF509E5, 0x02)  # $7E:09E5-$7E:09E6

    # --- Current formation ---
    CURRENT_FORMATION = (0xF5D123, 0x02)  # $7E:D123


# =============================================================================
# SnesABus Address Space - BW-RAM reads (needs testing, SA-1 dependent)
# These use SNES native addressing and require MemoryMapping=SA1
# =============================================================================

class BWRAMAddresses(AddressEnum):
    """BW-RAM addresses in SNES A-Bus address space. May or may not work
    depending on FxPak Pro / SNI SA-1 support."""

    # --- Event/progression flags ($00:7040-$00:709F) ---
    EVENT_FLAGS = (0x007040, 0x60)  # 96 bytes = 768 flag bits

    # --- Menu accessibility ---
    MENU_FLAGS = (0x007062, 0x01)

    # --- Map location flags ---
    MAP_DISCOVERY = (0x007065, 0x0C)  # $7065-$7070

    # --- Randomizer custom flags ---
    INVISIBLE_FLAGS_BYTE = (0x007089, 0x01)  # bit 5 = invisible flag 1
    CUSTOM_FLAGS_BYTE    = (0x00708C, 0x01)  # bits 1,5,6

    # --- Hidden chest counter ---
    HIDDEN_CHEST_COUNT = (0x0070C8, 0x01)

    # --- Boss victory counter ---
    BOSS_VICTORY_COUNT = (0x0070E3, 0x01)

    # --- Mario position/sprite ---
    MARIO_DATA = (0x006000, 0x5A)  # $6000-$6059


# =============================================================================
# SnesABus Address Space - IRAM reads (needs testing, SA-1 internal)
# =============================================================================

class IRAMAddresses(AddressEnum):
    """SA-1 IRAM addresses in SNES A-Bus address space. Most likely to fail
    on real hardware since this is SA-1 internal RAM."""

    # --- Current area (2 bytes) ---
    CURRENT_AREA = (0x003030, 0x02)

    # --- Party character slots ---
    PARTY_SLOTS = (0x003032, 0x0E)  # $3032-$303F (6 bytes chars + other)

    # --- Number of characters in party ---
    PARTY_COUNT = (0x00303F, 0x01)


# =============================================================================
# Alternate BW-RAM access via bank $40 mirror
# $40:0000-$40:FFFF mirrors SA-1 BW-RAM
# =============================================================================

class BWRAMMirrorAddresses(AddressEnum):
    """Alternate BW-RAM addresses via $40 bank mirror."""

    EVENT_FLAGS = (0x407040, 0x60)
    MENU_FLAGS  = (0x407062, 0x01)
    MAP_DISCOVERY = (0x407065, 0x0C)
    CURRENT_AREA_ALT = (0x403030, 0x02)
    PARTY_SLOTS_ALT  = (0x403032, 0x0E)
    PARTY_COUNT_ALT  = (0x40303F, 0x01)
    HIDDEN_CHEST_COUNT = (0x4070C8, 0x01)


# =============================================================================
# Character definitions
# =============================================================================

CHARACTER_NAMES = {
    0: "Mario",
    1: "Peach",
    2: "Bowser",
    3: "Geno",
    4: "Mallow",
}

# Offsets within a character stat block (0x25 bytes each)
# Based on $7F:F800 structure
class CharStatOffset:
    LEVEL        = 0x00  # 1 byte
    CURRENT_HP   = 0x01  # 2 bytes
    MAX_HP       = 0x03  # 2 bytes
    SPEED        = 0x05  # 1 byte
    ATTACK       = 0x06  # 1 byte
    DEFENSE      = 0x07  # 1 byte
    MG_ATTACK    = 0x08  # 1 byte
    MG_DEFENSE   = 0x09  # 1 byte
    CURRENT_EXP  = 0x0A  # 2 bytes
    WEAPON       = 0x0C  # 1 byte
    ARMOR        = 0x0D  # 1 byte
    ACCESSORY    = 0x0E  # 1 byte
    # ... additional fields follow


# =============================================================================
# Area name lookup
# =============================================================================

AREA_NAMES = {
    0: "To Mario's Pad (Before)",
    1: "Inner Factory",
    2: "To Mario's Pad",
    3: "Vista Hill",
    4: "Bowser's Keep",
    5: "Gate",
    6: "To Nimbus Land",
    7: "To Bowser's Keep",
    8: "Mario's Pad",
    9: "Mushroom Way",
    10: "Mushroom Kingdom",
    11: "Bandits Way",
    12: "Kero Sewers",
    13: "To Mushroom Kingdom",
    14: "Kero Sewers",
    15: "Midas River",
    16: "Tadpole Pond",
    17: "Rose Way",
    18: "Rose Town",
    19: "Forest Maze",
    20: "Pipe Vault",
    21: "To Yoster Isle",
    22: "To Moleville",
    23: "To Pipe Vault",
    24: "Moleville",
    25: "Booster Pass",
    26: "Booster Tower",
    27: "Booster Hill",
    28: "Marrymore",
    29: "To Star Hill",
    30: "To Marrymore",
    31: "Star Hill",
    32: "Seaside Town",
    33: "Sea",
    34: "Sunken Ship",
    35: "To Land's End",
    36: "To Seaside Town",
    37: "Land's End",
    38: "Monstro Town",
    39: "Bean Valley",
    40: "Grate Guy's Casino",
    41: "To Nimbus Land",
    42: "To Seaside Town",
    43: "Land's End",
    44: "Monstro Town",
    45: "Bean Valley",
    46: "Grate Guy's Casino",
    47: "To Nimbus Land",
    48: "To Bean Valley",
    49: "Nimbus Land",
    50: "Barrel Volcano",
    51: "To Bowser's Keep",
    52: "Yoster Isle",
    53: "To Pipe Vault",
    54: "Coal Mines (Bowser's Keep)",
    55: "Factory (Bowser's Keep)",
}


# =============================================================================
# Event flag definitions - (byte_offset_from_7040, bit) -> human name
# Only includes named/known flags relevant to progression tracking
# =============================================================================

EVENT_FLAGS = {
    # Boss defeats
    (0x12, 0): "Factory Boss Defeated",        # $7052 bit 0
    (0x13, 4): "Tower Boss 1 Defeated",        # $7053 bit 4
    (0x14, 2): "Keep Boss 2 Defeated",         # $7054 bit 2
    (0x15, 2): "Sewer Boss Defeated",          # $7055 bit 2
    (0x16, 5): "Mines Boss 1 Defeated",        # $7056 bit 5
    (0x16, 3): "Mines Boss 2 Defeated",        # $7056 bit 3
    (0x3E, 0): "Volcano Midboss Defeated",     # $707E bit 0
    (0x4A, 0): "Temple Boss Defeated",         # $708A bit 0
    (0x4B, 5): "Tower Boss 2 Defeated",        # $708B bit 5
    (0x4C, 3): "Bean Valley Boss Defeated",    # $708C bit 3
    (0x4F, 7): "Abyss Boss 1 Defeated",       # $708F bit 7
    (0x56, 0): "Abyss Boss 2 Defeated",        # $7096 bit 0
    (0x53, 6): "Keep Boss 1 Defeated",         # $7093 bit 6
    (0x53, 7): "Keep Boss 3 Defeated",         # $7093 bit 7

    # Dojo bosses
    (0x4A, 2): "Dojo Boss 1 Defeated",         # $708A bit 2
    (0x4A, 3): "Dojo Boss 2 Defeated",         # $708A bit 3
    (0x4A, 4): "Dojo Boss 3 Defeated",         # $708A bit 4
    (0x4A, 5): "Dojo Boss 4 Defeated",         # $708A bit 5

    # Area liberation
    (0x42, 0): "Mushroom Kingdom Liberated",   # $7082 bit 0
    (0x43, 6): "Forest Liberated",             # $7083 bit 6
    (0x0D, 3): "Bandits Way Liberated",        # $704D bit 3
    (0x0C, 6): "Marrymore Liberated",          # $704C bit 6
    (0x18, 7): "Ship Liberated",               # $7058 bit 7
    (0x46, 0): "Seaside Liberated",            # $7086 bit 0
    (0x1F, 4): "Nimbus Land Liberated",        # $705F bit 4
    (0x3D, 7): "Volcano Liberated",            # $707D bit 7
    (0x09, 7): "Yoster Isle Liberated 1",      # $7049 bit 7
    (0x1E, 2): "Yoster Isle Liberated 2",      # $705E bit 2

    # Character recruitment
    (0x13, 7): "Tower Character Recruited",    # $7053 bit 7

    # Star piece gates
    (0x11, 0): "Sea Gated by Star Pieces",     # $7051 bit 0
    (0x11, 1): "Keep Gated by Star Pieces",    # $7051 bit 1
    (0x11, 3): "Factory Gated by Star Pieces", # $7051 bit 3
    (0x11, 6): "Win Condition: Star Pieces",   # $7051 bit 6
    (0x11, 7): "Win Condition: Monstro Door",  # $7051 bit 7

    # Menu unlocks
    (0x22, 0): "Map Menu Unlocked",            # $7062 bit 0
    (0x22, 1): "Star Piece Menu Unlocked",     # $7062 bit 1
    (0x22, 2): "Switch Menu Unlocked",         # $7062 bit 2
    (0x22, 3): "Beetlemania Unlocked",         # $7062 bit 3

    # Star pieces (signal ring tracking)
    (0x41, 1): "Mimic 3 Star Piece",           # $7081 bit 1
    (0x41, 2): "Statue Keeper Star Piece",     # $7081 bit 2
    (0x41, 3): "Tower Boss 1 Star Piece",      # $7081 bit 3
    (0x41, 4): "Land's End Cloud Star Piece",  # $7081 bit 4
    (0x52, 4): "Battle Door Star Piece",       # $7092 bit 4

    # Map location discovery
    (0x25, 1): "Map: Mario's Pad",             # $7065 bit 1
    (0x25, 2): "Map: Mushroom Way",            # $7065 bit 2
    (0x25, 3): "Map: Mushroom Kingdom",        # $7065 bit 3
    (0x25, 4): "Map: Bandits Way",             # $7065 bit 4
    (0x26, 2): "Map: Rose Town",               # $7066 bit 2
    (0x26, 3): "Map: Forest Maze",             # $7066 bit 3
    (0x26, 4): "Map: Pipe Vault",              # $7066 bit 4
    (0x26, 5): "Map: Yoster Isle",             # $7066 bit 5
    (0x26, 6): "Map: Moleville",               # $7066 bit 6
    (0x26, 7): "Map: Booster Pass",            # $7066 bit 7
    (0x27, 0): "Map: Booster Tower",           # $7067 bit 0
    (0x27, 1): "Map: Marrymore",               # $7067 bit 1
    (0x27, 2): "Map: Star Hill",               # $7067 bit 2
    (0x27, 3): "Map: Seaside Town",            # $7067 bit 3
    (0x27, 4): "Map: Sea",                     # $7067 bit 4
    (0x27, 5): "Map: Sunken Ship",             # $7067 bit 5
    (0x27, 6): "Map: Land's End",              # $7067 bit 6
    (0x27, 7): "Map: Monstro Town",            # $7067 bit 7
    (0x28, 0): "Map: Bean Valley",             # $7068 bit 0
    (0x28, 1): "Map: Nimbus Land",             # $7068 bit 1
    (0x28, 2): "Map: Barrel Volcano",          # $7068 bit 2
    (0x28, 3): "Map: Vista Hill",              # $7068 bit 3
    (0x28, 4): "Map: Booster Hill",            # $7068 bit 4
    (0x28, 5): "Map: Gate",                    # $7068 bit 5
    (0x28, 6): "Map: Casino",                  # $7068 bit 6

    # Inner factory rooms
    (0x19, 4): "Inner Factory Room 1 Completed",  # $7059 bit 4
    (0x50, 3): "Inner Factory Room 2 Completed",  # $7090 bit 3
    (0x51, 3): "Inner Factory Room 3 Completed",  # $7091 bit 3
    (0x4F, 6): "Inner Factory Room 4 Completed",  # $708F bit 6

    # Misc progression
    (0x13, 6): "Tower Opened",                 # $7053 bit 6
    (0x0D, 7): "Booster Hill Cleared",         # $704D bit 7
    (0x17, 4): "Minecart Cleared",             # $7057 bit 4
    (0x18, 6): "Ship Midboss Completed",       # $7058 bit 6
    (0x19, 0): "Casino Prize Won",             # $7059 bit 0
    (0x12, 2): "Belome Temple Open",           # $7052 bit 2
    (0x4E, 5): "Gave Seed",                    # $708E bit 5
    (0x4E, 6): "Gave Fertilizer",              # $708E bit 6
    (0x4E, 7): "Gave Seed and Fertilizer",     # $708E bit 7
    (0x55, 3): "Star Hill Checked",            # $7095 bit 3
    (0x1F, 5): "Nimbus Mid Boss Completed",    # $705F bit 5
    (0x50, 2): "Nimbus Boss in Town Square",   # $7090 bit 2
    (0x53, 1): "Statue Keeper Fight Completed",  # $7093 bit 1

    # Sunken Ship sub-events
    (0x17, 5): "Mimic 1 Cleared",             # $7057 bit 5
    (0x17, 7): "Mimic 2 Cleared",             # $7057 bit 7
    (0x24, 6): "Mimic 3 Cleared",             # $7064 bit 6

    # Key items / exchanges
    (0x55, 5): "Cricket Pie Exchanged",        # $7095 bit 5
    (0x1E, 4): "Shiny Stone Traded",           # $705E bit 4
    (0x59, 0): "Smithy Boss Hunt Win Condition",  # $7099 bit 0

    # Prizes
    (0x52, 0): "Super Jump Prize 1 Granted",   # $7092 bit 0
    (0x52, 2): "Super Jump Prize 2 Granted",   # $7092 bit 2
    (0x59, 4): "Goomba Thumpin Prize 1",       # $7099 bit 4
    (0x59, 5): "Goomba Thumpin Prize 2",       # $7099 bit 5
    (0x59, 6): "Knife Guy Prize Granted",      # $7099 bit 6

    # Fast travel
    (0x4B, 0): "Fast Travel Enabled",          # $708B bit 0
    (0x1E, 6): "Bucket Warp Enabled",          # $705E bit 6
    (0x48, 5): "Casino Warp Enabled",          # $7088 bit 5
}


# =============================================================================
# Helper functions
# =============================================================================

def parse_character_stats(data: bytes, char_index: int) -> dict:
    """Parse a character stat block from the CHARACTER_BLOCK read.

    Args:
        data: Raw bytes from CHARACTER_BLOCK read (0xB9 bytes total)
        char_index: 0=Mario, 1=Peach, 2=Bowser, 3=Geno, 4=Mallow
    Returns:
        Dict with parsed stat values
    """
    offset = char_index * 0x25
    block = data[offset:offset + 0x25]

    return {
        "name": CHARACTER_NAMES.get(char_index, f"Unknown({char_index})"),
        "level": block[0x00],
        "current_hp": int.from_bytes(block[0x01:0x03], "little"),
        "max_hp": int.from_bytes(block[0x03:0x05], "little"),
        "speed": block[0x05],
        "attack": block[0x06],
        "defense": block[0x07],
        "mg_attack": block[0x08],
        "mg_defense": block[0x09],
        "experience": int.from_bytes(block[0x0A:0x0C], "little"),
        "weapon": block[0x0C],
        "armor": block[0x0D],
        "accessory": block[0x0E],
    }


def parse_event_flags(data: bytes) -> dict[str, bool]:
    """Parse event flag bytes into named flags.

    Args:
        data: Raw bytes from EVENT_FLAGS read (96 bytes, $7040-$709F)
    Returns:
        Dict mapping flag name to True/False
    """
    result = {}
    for (byte_offset, bit), name in EVENT_FLAGS.items():
        if byte_offset < len(data):
            result[name] = bool(data[byte_offset] & (1 << bit))
    return result


def get_area_name(area_id: int) -> str:
    """Get human-readable area name from area ID."""
    return AREA_NAMES.get(area_id, f"Unknown Area ({area_id})")


def parse_party(data: bytes) -> list[str]:
    """Parse party slot data into character names.

    Args:
        data: Raw bytes from PARTY_SLOTS read
    Returns:
        List of character names currently in party
    """
    party = []
    for i in range(min(len(data), 5)):
        char_id = data[i]
        if char_id < 5:
            party.append(CHARACTER_NAMES[char_id])
    return party
