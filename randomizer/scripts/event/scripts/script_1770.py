# pylint: disable=C0301

"""E1770_TEMPLE_FORTUNE_RESULTS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(HAS_A_PRIZE_FORTUNE, ["EVENT_1770_remove_from_current_level_4"]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            mod_id=0,
        ),
        ActionQueueAsync(
            target=LAYER_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftSouthSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Jmp(["EVENT_1770_jmp_to_event_5"]),
        RemoveObjectFromCurrentLevel(
            NPC_4, identifier="EVENT_1770_remove_from_current_level_4"
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1770_jmp_to_event_5"),
    ]
)
