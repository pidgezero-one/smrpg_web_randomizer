"""A0453_FACTORY_FOUR_SCREW_ROOM_AMEBOID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        JmpIfBitClear(DIRECTIONAL_7045_7, ["ACTION_453_pause_3"]),
        Pause(176),
        Pause(1, identifier="ACTION_453_pause_3"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=4,
            destinations=["ACTION_453_sequence_looping_on_6"]),
        Jmp(["ACTION_453_pause_3"]),
        SequenceLoopingOn(identifier="ACTION_453_sequence_looping_on_6"),
        SetSpriteSequence(index=8, looping=False),
        Pause(48),
        WalkNortheastSteps(2, identifier="ACTION_453_shift_northeast_steps_9"),
        WalkNorthwestSteps(2),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(2),
        Jmp(["ACTION_453_shift_northeast_steps_9"]),
    ]
)
