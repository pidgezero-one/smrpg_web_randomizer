"""A0883_INC_PALETTE_ROW_FAKE_BIRD_STATUE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        IncPaletteRowBy(1),
        Pause(1, identifier="ACTION_883_pause_1"),
        JmpIfObjectWithinRange(
            comparing_npc=MARIO, usually=0, tiles=2, destinations=["ACTION_883_pause_4"]
        ),
        Jmp(["ACTION_883_pause_1"]),
        Pause(30, identifier="ACTION_883_pause_4"),
        SequenceLoopingOn(),
        IncPaletteRowBy(15),
        Jmp(["ACTION_881_set_solidity_bits_0"]),
    ]
)
