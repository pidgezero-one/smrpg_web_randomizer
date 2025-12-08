# pylint: disable=C0301

"""E0278_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MEM_70A9,
            subscript=[
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_278_action_queue_async_0_SUBSCRIPT_pause_3"
                ),
                ASJmpIfObjectInAir(
                    MEM_70A9, ["EVENT_278_action_queue_async_0_SUBSCRIPT_pause_3"]
                ),
                ASCopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_700C),
                ASJmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_278_ret_1"]),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        Return(identifier="EVENT_278_ret_1"),
    ]
)
