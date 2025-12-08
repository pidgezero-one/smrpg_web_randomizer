# pylint: disable=C0301,C0103

"""referenced by monster_attacks GetTough"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=82,
    script=[
        RunSubroutine(["command_0x35259b"], identifier="queuestart_0x357348"),
        Db(bytearray(b"\x83\x83")),
        ResetObjectMappingMemory(),
        MoveObject(
            speed=1,
            start_position=-257,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True),
        MoveObject(
            speed=33,
            start_position=-769,
            end_position=0,
            apply_to_y=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=30),
        ResetObjectMappingMemory(),
        MoveObject(
            speed=1,
            start_position=-257,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True),
        MoveObject(
            speed=33,
            start_position=0,
            end_position=992,
            apply_to_y=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=30),
        ResetObjectMappingMemory(),
        PlaySound(sound=S0038_FRYING_PAN_HIT_2),
        MoveObject(
            speed=1,
            start_position=96,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True),
        MoveObject(
            speed=1,
            start_position=96,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True),
        MoveObject(
            speed=33,
            start_position=-513,
            end_position=512,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=32),
        ResetObjectMappingMemory(),
        Jmp(["command_0x356af4"]),
    ])
