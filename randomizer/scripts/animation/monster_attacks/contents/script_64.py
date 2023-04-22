"""DarkClaw animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        SpriteSequence(sequence=5),
        PauseScriptUntilSpriteSequenceDone(),
        ResetSpriteSequence(),
        PlaySound(sound=S0108_HOWL),
        SetAMEM16BitToConst(0x60, 13),
        RunSubroutine(["command_0x352475"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x35242a"]),
        ReturnSubroutine(),
    ]
)
