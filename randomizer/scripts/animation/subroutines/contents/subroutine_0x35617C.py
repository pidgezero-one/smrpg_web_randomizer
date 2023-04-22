# pylint: disable=C0301,C0103

"""referenced by monster_attacks PsychoPlasm"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=49,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x35617c"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=0,
            y=-16,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        Db(bytearray(b" \xbeC\x00")),
        JmpIfAMEM8BitNotEqualsConst(0x6E, 4, ["command_0x35253b"]),
        PlaySound(sound=S0037_MONSTER_ITEM_TOSS),
        EnableSpritesOnSubscreen(),
        NewSpriteAtCoords(
            sprite_id=SPR0801_SLEEP_ZZZ_S,
            sequence=0,
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
