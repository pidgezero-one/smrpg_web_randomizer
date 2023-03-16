"""Enums supporting NPC classes and functions."""

from enum import IntEnum


class VramStore(IntEnum):
    """Defines how many directions an NPC will be allowed to face.\n
    For example, a NPC with only SWSE who tries to face north will
    simply have its south-facing sprites (sequence 0) loaded instead,
    but an NPC with SWSE/NWSE will actually be able to use its north-facing
    sprites (sequence 1) when it faces north.\n
    It is generally better to support as few directions as necessary for a NPC.
    There is no real use loading NWNE molds into VRAM for a NPC who you don't expect
    to face north in that room."""

    DIR0_SWSE_NWNE = 0
    DIR1_SWSE_NWNE_S = 1
    DIR2_SWSE = 2
    DIR3_SWSE_NWNE = 3
    DIR4_ALL_DIRECTIONS = 4
    DIR5_UNKNOWN = 5
    DIR6_UNKNOWN = 6
    DIR7_ALL_DIRECTIONS = 7


class ShadowSize(IntEnum):
    """The different shadow shapes available for any NPC."""

    OVAL_SMALL = 0
    OVAL_MED = 1
    OVAL_BIG = 2
    BLOCK = 3
