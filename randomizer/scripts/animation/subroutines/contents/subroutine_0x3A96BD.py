# pylint: disable=C0301,C0103

"""referenced by"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=96,
    script=[
        PlaySound(sound=S0110_HUGE_EXPLOSION),
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION, x=16, y=0, z=0, set_x=True, set_y=True, set_z=True
        ),
        NewEffectObject(effect=EF0059_ORANGE_RED_BLAST__FIRE_BOMB_, looping_off=True),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        PauseScriptUntil(condition=SEQ_4BPP_COMPLETE),
        RunSubroutine(["command_0x3a755e"]),
        Db(bytearray(b"[\x07\x00")),
        ReturnObjectQueue(),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=8,
            y=0,
            z=-128,
            set_x=True,
            set_y=True,
            set_z=True),
        NewSpriteAtCoords(
            sprite_id=SPR0792_BLACK_ROCK,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        MoveObject(
            speed=65,
            start_position=2048,
            end_position=4096,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ResetObjectMappingMemory(),
        RunSubroutine(["command_0x3a8698"]),
        MoveObject(
            speed=1,
            start_position=-1025,
            end_position=-1025,
            apply_to_z=True,
            should_set_end_position=True,
            should_set_speed=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        ResetObjectMappingMemory(),
        SpriteSequence(sequence=1),
        PauseScriptUntilSpriteSequenceDone(),
        RemoveObject(),
        ClearAMEM8Bit(0x60),
        ClearAMEM8Bit(0x67),
        ClearAMEM8Bit(0x68),
        SetAMEM16BitToConst(0x60, 1),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A87CA),
        RunSubroutine(["command_0x3a8674"]),
        RunSubroutine(["command_0x3a7622"]),
        ReturnObjectQueue(),
    ])
