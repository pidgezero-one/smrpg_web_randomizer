# pylint: disable=C0301,C0103

"""referenced by behaviour_17_0x35096F"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=23,
    script=[
        PlaySound(sound=S0013_COIN, identifier="queuestart_0x3508ff"),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0192_COIN, sequence=2, store_to_vram=True, store_palette=True
        ),
        ResetTargetMappingMemory(),
        MoveObject(
            speed=25,
            start_position=-769,
            end_position=0,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
        ),
        Db(bytearray(b"\x12\x81")),
        PauseScriptUntilSpriteSequenceDone(),
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ],
)
