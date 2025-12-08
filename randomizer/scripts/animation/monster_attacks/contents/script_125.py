"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        PlaySound(sound=S0169_TELEPORT_ATTACK),
        RunSubroutine(["command_0x357ebe"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0451_JINX_2,
            sequence=6,
            store_to_vram=True,
            store_palette=True),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0110_HUGE_EXPLOSION),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0451_JINX_3,
            sequence=0,
            store_to_vram=True,
            store_palette=True),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x35358a"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
