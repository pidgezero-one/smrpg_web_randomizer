"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        RunSubroutine(["command_0x357b73"]),
        PlaySound(sound=S0035_SPELL_POWER_UP),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0451_JINX_2,
            sequence=4,
            store_to_vram=True,
            store_palette=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        PlaySound(sound=S0102_STATIC_E),
        SetAMEM16BitToConst(0x60, 28),
        RunSubroutine(["command_0x352475"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0451_JINX_3,
            sequence=0,
            store_to_vram=True,
            store_palette=True),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x3535ad"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
