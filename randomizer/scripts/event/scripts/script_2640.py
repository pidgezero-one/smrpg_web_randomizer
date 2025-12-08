# pylint: disable=C0301

"""E2640_BOOSTER_PASS_RIGHT_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_2640_grant"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(3),
                ASClearBit(UNIVERSAL_CHEST_ANIMATION_BIT),
            ]),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_2640_grant"),
        Return(),
    ]
)
