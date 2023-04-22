"""A0473_BANDITS_WAY_5_TROOPA_INIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(3),
        EndLoop(),
        ShadowOn(),
        Db(bytearray(b" \x05")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x10\x00\x01\x00\x00\x00\x04\x80")
        ),
        WalkNorthwestSteps(14, identifier="ACTION_473_shift_northwest_steps_9"),
        Walk1StepNortheast(),
        WalkSoutheastSteps(14),
        Walk1StepSouthwest(),
        Jmp(["ACTION_473_shift_northwest_steps_9"]),
    ]
)
