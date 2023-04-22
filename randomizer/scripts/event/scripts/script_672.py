# pylint: disable=C0301

"""E0672_MARRYMORE_OCCUPIED_EXTERIOR_CHAPEL_FRONT_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, mod_id=0
        ),
        Return(),
    ]
)
