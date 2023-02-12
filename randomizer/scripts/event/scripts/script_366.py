# E0366_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_FORCED_OFF_MINION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(32),
                ASShiftSoutheastSteps(2),
                ASPause(
                    1, identifier="EVENT_366_action_queue_async_0_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(["EVENT_366_action_queue_async_0_SUBSCRIPT_pause_2"]),
            ],
        ),
        Return(),
    ]
)
