"""FlutterHush animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3577e2"]),
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        SpriteSequence(sequence=3),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0081_WALLOP_2),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"]),
        ReturnSubroutine(),
    ]
)
