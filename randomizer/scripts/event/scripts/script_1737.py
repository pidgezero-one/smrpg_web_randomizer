# pylint: disable=C0301

"""E1737_SKY_BRIDGE_DONUT_LIFT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioOnAnObjectOrNot(["EVENT_1737_jmp_if_bit_set_4", "EVENT_1737_ret_3"]),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_1737_ret_3"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASJumpToHeight(153),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastPixels(20),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASWalkSoutheastPixels(50),
                ASSetWalkingSpeed(FAST),
            ],
        ),
        Return(identifier="EVENT_1737_ret_3"),
        JmpIfBitSet(
            SKY_BRIDGE_COURSE_CHOICE,
            ["EVENT_1846_jmp_if_bit_set_0"],
            identifier="EVENT_1737_jmp_if_bit_set_4",
        ),
        Return(),
    ]
)
