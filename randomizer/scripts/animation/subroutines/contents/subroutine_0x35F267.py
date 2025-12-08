# pylint: disable=C0301,C0103

"""referenced by weapons TroopaShell"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=74,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=10,
            y=-12,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35f267"),
        NewSpriteAtCoords(
            sprite_id=SPR0539_ORANGE_LAZY_SHELL,
            sequence=1,
            priority=3,
            vram_address=0x6600,
            palette_row=8,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True),
        PlaySound(sound=S0018_SUPER_JUMP_HIT_1),
        MoveObject(
            speed=161,
            start_position=-2561,
            end_position=2560,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True),
        Pause1Frame(),
        PauseScriptUntil(condition=BUTTON_PRESSED),
        ResetObjectMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=4,
            y=-6,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1920, arch_height=0),
        PlaySound(sound=S0058_SUPER_JUMP_HIT_2),
        RemoveObject(),
        NewSpriteAtCoords(
            sprite_id=SPR0539_ORANGE_LAZY_SHELL,
            sequence=1,
            priority=3,
            vram_address=0x6600,
            palette_row=8,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        SetAMEM8BitToConst(0x67, 1),
        SetOMEMMainToAMEM8Bit(omem=0x67, amem=0x67),
        RemoveObject(),
        ReturnObjectQueue(),
    ])
