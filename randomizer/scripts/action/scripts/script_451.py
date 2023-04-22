"""A0451_FACTORY_FOUR_SCREW_ROOM_AMEBOID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        JmpIfBitClear(DIRECTIONAL_7045_7, ["ACTION_451_pause_3"]),
        Pause(176),
        Pause(1, identifier="ACTION_451_pause_3"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=3,
            destinations=["ACTION_451_sequence_looping_on_6"],
        ),
        Jmp(["ACTION_451_pause_3"]),
        SequenceLoopingOn(identifier="ACTION_451_sequence_looping_on_6"),
        SetSpriteSequence(index=8, looping=False),
        Pause(48),
        Walk1StepSouthwest(),
        Walk1StepSoutheast(),
        WalkNortheastSteps(2),
        Walk1StepSouthwest(identifier="ACTION_451_walk_1_step_southwest_12"),
        Walk1StepNorthwest(),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(2),
        WalkNortheastSteps(3),
        Walk1StepNorthwest(),
        Jmp(["ACTION_451_walk_1_step_southwest_12"]),
    ]
)
