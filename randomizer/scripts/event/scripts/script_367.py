# pylint: disable=C0301

"""E0367_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_FORCED_OFF_MINION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(32),
                ASWalkNorthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_367_action_queue_async_0_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(["EVENT_367_action_queue_async_0_SUBSCRIPT_pause_2"]),
            ]),
        Return(),
    ]
)
