# pylint: disable=C0301,C0103

"""referenced by monster_spells DiamondSaw, monster_spells PetalBlast"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=112,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35664f"),
        NewSpriteAtCoords(
            sprite_id=SPR0782_DIAMOND_SAW_SNOWFLAKE,
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
        SetAMEM16BitToConst(0x60, 4),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=112),
        FadeOutSprite(duration=2),
        VisibilityOff(),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        Pause1Frame(identifier="command_0x356680"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 2, ["command_0x356680"]),
        Jmp(["command_0x356b01"]),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35668a"),
        NewSpriteAtCoords(
            sprite_id=SPR0544_SMALL_PINK_PETAL,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=8,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        ClearAMEM8Bit(0x64),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(
            index=28, target_address=0x356B15, identifier="command_0x3566a5"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 32, ["command_0x3566a5"]),
        Pause1Frame(identifier="command_0x3566b5"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 32, ["command_0x3566b5"]),
        Jmp(["command_0x356b01"]),
    ])
