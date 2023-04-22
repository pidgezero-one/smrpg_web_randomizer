# pylint: disable=C0301

"""E3378_KEEP_OPEN_DOOR_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(KEEP_DOORS_EXIT_TYPE_2, 32),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS,
            mod_id=39,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS,
            mod_id=45,
        ),
        CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
        Jmp(["EVENT_3376_clear_attempt_counter"]),
    ]
)
