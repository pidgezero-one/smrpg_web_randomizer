# pylint: disable=C0301

"""E1671_LANDS_END_1_INVISIBLE_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1671_ret_5"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(bits=[], destinations=["EVENT_1671_ret_5"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(22),
                ASJmpIfBitSet(TEMP_7043_1, ["EVENT_1671_ret_5"]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Return(identifier="EVENT_1671_ret_5"),
    ]
)
