# pylint: disable=C0301

"""E3299_OUTER_SEA_WHIRLPOOL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTurnClockwise45DegreesNTimes(
                    1,
                    identifier="EVENT_3299_action_queue_async_0_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1",
                ),
                ASShiftZUpPixels(2),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
                ASCompareVarToConst(PRIMARY_TEMP_700C, 1280),
                ASJmpIfLoadedMemoryIsAboveOrEqual0(
                    [
                        "EVENT_3299_action_queue_async_0_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1"
                    ]
                ),
                ASFloatingOn(),
                ASObjectMemorySetBit(arg_1=0x0C, bits=[3, 4, 5]),
            ],
        ),
        Return(),
    ]
)
