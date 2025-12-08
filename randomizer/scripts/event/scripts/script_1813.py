# pylint: disable=C0301

"""E1813_SAVE_BOX_IN_ROOMS_WITH_EXP_STARS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1813_action_queue_async_2"]),
        JmpToEvent(E0080_SAVE_BLOCK_SUBROUTINE),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(108),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_1813_action_queue_async_2_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1813_action_queue_async_2_SUBSCRIPT_pause_2"]
                ),
            ],
            identifier="EVENT_1813_action_queue_async_2"),
        Return(),
    ]
)
