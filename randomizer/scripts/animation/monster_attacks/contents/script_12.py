"""Thornet animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357ae5"]),
        SpriteSequence(sequence=3),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0080_WALLOP_1),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
