# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack31"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=32,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x356089"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=0,
            y=-16,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        EnableSpritesOnSubscreen(),
        NewSpriteAtCoords(
            sprite_id=SPR0517_BOMB_EXPLOSION,
            sequence=0,
            priority=0,
            vram_address=0x6200,
            palette_row=8,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        PauseScriptUntilSpriteSequenceDone(),
        FadeOutSprite(duration=2),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        VisibilityOff(),
        DisableSpritesOnSubscreen(),
        RunSubroutine(["command_0x35252f"]),
    ])
