# E1673_LANDS_END_2_INVISIBLE_PLATFORM_UPPER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1673_ret_5"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(destinations=["EVENT_1673_ret_5"]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(22),
                ASJmpIfBitSet(TEMP_7043_2, ["EVENT_1673_ret_5"]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        Return(identifier="EVENT_1673_ret_5"),
    ]
)
