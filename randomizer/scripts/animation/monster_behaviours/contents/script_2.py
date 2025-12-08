"""behaviour_2_0x350635 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=52,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        Db(bytearray(b"T")),
        Db(bytearray(b">")),
        SpriteSequence(sequence=13, looping_off=True),
        MoveObject(
            speed=1,
            start_position=256,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True),
        MoveObject(
            speed=1,
            start_position=-129,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ResetObjectMappingMemory(),
        MoveObject(
            speed=1,
            start_position=-257,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True),
        MoveObject(
            speed=1,
            start_position=128,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ResetObjectMappingMemory(),
        ResetSpriteSequence(),
        Jmp(["command_0x3506e2"]),
    ])
