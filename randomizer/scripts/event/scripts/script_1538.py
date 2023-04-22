# pylint: disable=C0301

"""E1538_BANDITS_WAY_STAR_CHEST_CAMERA_AND_DOGS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1538_run_background_event_2"]),
        SetBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        RunBackgroundEvent(
            event_id=E1706_BANDITS_WAY_LEFT_CHEST_STAR_CHECK,
            return_on_level_exit=True,
            bit_6=True,
            identifier="EVENT_1538_run_background_event_2",
        ),
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1538_jmp_to_event_4"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASClearBit(UNIVERSAL_CHEST_ANIMATION_BIT),
            ],
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_1538_jmp_to_event_4"),
    ]
)
