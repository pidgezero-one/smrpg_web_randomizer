# pylint: disable=C0301

"""E3382_KEEP_OPEN_DOOR_6"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(KEEP_DOORS_EXIT_TYPE_2, 96),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS,
            mod_id=43),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS,
            mod_id=49),
        CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000),
        Jmp(["EVENT_3376_clear_attempt_counter"]),
    ]
)
