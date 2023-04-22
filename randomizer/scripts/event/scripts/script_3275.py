# pylint: disable=C0301

"""E3275_SHIP_ZEOSTAR_STAIRWAY_OPEN_UNDERWATER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3275_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS,
            mod_id=0,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3275_ret_4"),
    ]
)
