"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        RunSubroutine(["command_0x357b73"]),
        PlaySound(sound=S0116_TERRAPIN_SWING),
        SpriteSequence(sequence=4),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=30),
        SpriteSequence(sequence=5, looping_off=True),
        RunSubroutine(["command_0x353005"]),
        RunSubroutine(["command_0x357ef0"]),
        PlaySound(sound=S0152_HIT),
        RunSubroutine(["command_0x3523c4"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
