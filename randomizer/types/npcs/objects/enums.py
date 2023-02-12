from enum import IntEnum


class VramStore(IntEnum):
    DIR0_SWSE_NWNE = 0
    DIR1_SWSE_NWNE_S = 1
    DIR2_SWSE = 2
    DIR3_SWSE_NWNE = 3
    DIR4_ALL_DIRECTIONS = 4
    DIR5_UNKNOWN = 5
    DIR6_UNKNOWN = 6
    DIR7_ALL_DIRECTIONS = 7


class ShadowSize(IntEnum):
    OVAL_SMALL = 0
    OVAL_MED = 1
    OVAL_BIG = 2
    BLOCK = 3
