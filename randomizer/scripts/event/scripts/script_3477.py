# pylint: disable=C0301

"""E3477_KINGDOM_HALLWAY_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_3477_j"]),
        DisableObjectTriggerInSpecificLevel(
            NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL
        ),
        DisableObjectTriggerInSpecificLevel(
            NPC_6, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL
        ),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3477_item_grant"], identifier="EVENT_3477_j"),
        SetBit(TEMP_7042_0),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftZUpSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownSteps(2),
                ASClearBit(TEMP_7042_0),
            ],
        ),
        UnfreezeCamera(),
        JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_3477_item_grant"),
    ]
)
