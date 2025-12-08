# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack47"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=93,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=-8,
            y=248,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3565a2"),
        NewSpriteAtCoords(
            sprite_id=SPR0804_GUNK_BALL_INK_BLAST,
            sequence=5,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        ClearAMEM8Bit(0x64),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(
            index=12, target_address=0x356B15, identifier="command_0x3565bd"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 10, ["command_0x3565bd"]),
        SpriteSequence(sequence=6),
        ClearAMEM8Bit(0x64),
        ObjectQueueAtOffsetAndIndex(
            index=12, target_address=0x356B15, identifier="command_0x3565d1"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 20, ["command_0x3565d1"]),
        SpriteSequence(sequence=7),
        ClearAMEM8Bit(0x64),
        ObjectQueueAtOffsetAndIndex(
            index=12, target_address=0x356B15, identifier="command_0x3565e5"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 30, ["command_0x3565e5"]),
        Pause1Frame(identifier="command_0x3565f5"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 60, ["command_0x3565f5"]),
        Jmp(["command_0x356b01"]),
    ])
