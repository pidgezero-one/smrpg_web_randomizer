# pylint: disable=C0301,C0103

"""referenced by monster_attacks Poison"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=70,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=6,
            y=200,
            z=8,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3564d7",
        ),
        EnableSpritesOnSubscreen(),
        NewSpriteAtCoords(
            sprite_id=SPR0794_DARK_RED_YELLOW_FIREBALL,
            sequence=0,
            priority=0,
            vram_address=0x6200,
            palette_row=8,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        FadeInSprite(duration=2),
        VisibilityOn(),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        ClearAMEM8Bit(0x64),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(
            index=20, target_address=0x356B15, identifier="command_0x3564f8"
        ),
        ObjectQueueAtOffsetAndIndex(index=22, target_address=0x356B15),
        Pause1Frame(),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 6, ["command_0x3564f8"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=55),
        FadeOutSprite(duration=2),
        VisibilityOff(),
        Pause1Frame(identifier="command_0x356512"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 12, ["command_0x356512"]),
        DisableSpritesOnSubscreen(),
        Jmp(["command_0x356b01"]),
    ],
)
