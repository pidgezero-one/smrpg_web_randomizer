"""A0970_ENDING_CREDITS_CASTLE_TERRAPINS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FASTEST),
        Walk1StepNorthwest(),
        WalkNorthwestPixels(4),
        FaceNortheast(),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 21, ["ACTION_970_start_loop_n_times_15"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 22, ["ACTION_970_start_loop_n_times_23"]
        ),
        StartLoopNTimes(9),
        SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
        Pause(34),
        EndLoop(),
        SetSpriteSequence(
            index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(80),
        SetSpriteSequence(
            index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Return(),
        StartLoopNTimes(10, identifier="ACTION_970_start_loop_n_times_15"),
        SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
        Pause(34),
        EndLoop(),
        SetSpriteSequence(
            index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(64),
        SetSpriteSequence(
            index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Return(),
        StartLoopNTimes(11, identifier="ACTION_970_start_loop_n_times_23"),
        SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
        Pause(34),
        EndLoop(),
        SetSpriteSequence(
            index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(48),
        SetSpriteSequence(
            index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Return(),
    ]
)
