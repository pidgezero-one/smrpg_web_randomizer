# referenced by weapons DoublePunch

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=56,
    script=[
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=34, identifier="queuestart_0x35f96a"
        ),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=20,
            y=-20,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        NewSpriteAtCoords(
            sprite_id=SPR0028_GENO_ELBOW_SHOT,
            sequence=3,
            priority=3,
            vram_address=0x6600,
            palette_row=8,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        PlaySound(sound=S0051_FIRE_THROW_BIG),
        ResetTargetMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=0,
            y=-8,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1792, arch_height=0),
        PlaySound(sound=S0051_FIRE_THROW_BIG),
        PauseScriptUntil(condition=0x07),
        RemoveObject(),
        SetAMEM8BitToConst(0x66, 1),
        SetOMEMMainToAMEM8Bit(omem=0x66, amem=0x66),
        ResetObjectMappingMemory(),
        ReturnObjectQueue(),
    ],
)
