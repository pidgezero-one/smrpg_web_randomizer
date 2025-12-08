# pylint: disable=C0301,C0103

"""referenced by monster_attacks GetTough"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=63,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=248,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35696b"),
        NewSpriteAtCoords(
            sprite_id=SPR0545_THROWN_HAMMER,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=8,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        SetAMEM16BitToConst(0x60, 7),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=12),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=12),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=12),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        Pause1Frame(identifier="command_0x3569a0"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 4, ["command_0x3569a0"]),
        Jmp(["command_0x356b01"]),
    ])
