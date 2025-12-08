# pylint: disable=C0301

"""E3310_SHIP_HIDDEN_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(2),
                ASShiftSouthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=MARIO, subscript=[ASFloatingOff(), ASPause(4), ASFloatingOn()]
        ),
        RunBackgroundEvent(
            event_id=E3228_SHIP_CLONE_CONTROL, return_on_level_exit=True
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
    ]
)
