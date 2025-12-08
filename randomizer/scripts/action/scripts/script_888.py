"""A0888_NIMBUS_SOLO_FAKE_BIRD_STATUE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        IncPaletteRowBy(1),
        Pause(1, identifier="ACTION_888_pause_1"),
        JmpIfObjectWithinRange(
            comparing_npc=MARIO,
            usually=0,
            tiles=2,
            destinations=["ACTION_888_sequence_looping_on_4"]),
        Jmp(["ACTION_888_pause_1"]),
        SequenceLoopingOn(identifier="ACTION_888_sequence_looping_on_4"),
        Pause(30),
        IncPaletteRowBy(15),
        Jmp(["ACTION_881_set_solidity_bits_0"]),
    ]
)
