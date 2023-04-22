# pylint: disable=C0301

"""E3687_MARRYMORE_SHOWER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_7, ["EVENT_3584_ret_0"]),
        SetBit(TEMP_7044_7),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1
        ),
        Return(),
    ]
)
