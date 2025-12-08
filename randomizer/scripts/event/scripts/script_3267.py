# pylint: disable=C0301

"""E3267_SHIP_LOWER_RAT_STAIRWAY_OPEN_LOWER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3267_ret_6"]),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS,
            mod_id=33),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_1),
        Store00To0248(),
        Return(identifier="EVENT_3267_ret_6"),
    ]
)
