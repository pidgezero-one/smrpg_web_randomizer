# E3626_NIMBUS_SHOP_CHEST_CAMERA_SHIFT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3584_ret_0"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R344_NIMBUS_LAND_ITEM_SHOP, ["EVENT_3584_ret_0"]
        ),
        SetBit(TEMP_7043_0),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalk1StepNorth(),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepNorth(),
            ],
        ),
        Return(),
    ]
)
