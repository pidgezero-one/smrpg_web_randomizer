# pylint: disable=C0301

"""E3880_SEA_CHESTS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_3880_npc"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(2),
                ASShiftSouthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 21, ["EVENT_3880_chest_2"], identifier="EVENT_3880_npc"
        ),
        JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3880_chest_3"]),
        JmpToEvent(E0174_CHEST_3_CONTAINER),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_3880_chest_2"),
        JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_3880_chest_3"),
    ]
)
