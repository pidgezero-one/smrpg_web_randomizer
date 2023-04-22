# pylint: disable=C0301,C0103

"""referenced by monster_attacks Endobubble"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=49,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x3561af"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=0,
            y=-32,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        Db(bytearray(b" \xbeC\x00")),
        JmpIfAMEM8BitNotEqualsConst(0x6E, 4, ["command_0x35253b"]),
        PlaySound(sound=S0029_FIRE_SHOOT),
        EnableSpritesOnSubscreen(),
        NewSpriteAtCoords(
            sprite_id=SPR0551_MUTE_BALLOON,
            sequence=3,
            priority=0,
            vram_address=0x6200,
            palette_row=8,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        FadeInSprite(duration=2),
        VisibilityOn(),
        PauseScriptUntilSpriteSequenceDone(),
        FadeOutSprite(duration=2),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        VisibilityOff(),
        DisableSpritesOnSubscreen(),
        RunSubroutine(["command_0x35252f"]),
    ],
)
