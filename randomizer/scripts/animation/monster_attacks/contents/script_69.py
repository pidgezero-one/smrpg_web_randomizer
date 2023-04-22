"""SomnusWaltz animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351bfd"]),
        RunSubroutine(["command_0x3577e2"]),
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        SpriteSequence(sequence=4),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        PlaySound(sound=S0156_CHOMP_BITE),
        PauseScriptUntilSpriteSequenceDone(),
        ResetSpriteSequence(),
        Jmp(["command_0x351bcd"]),
        SetOMEM60To072C(identifier="command_0x351bfd"),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        SpriteSequence(sequence=3),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        PlaySound(sound=S0156_CHOMP_BITE),
        PauseScriptUntilSpriteSequenceDone(),
        ResetSpriteSequence(),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351c17"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"], identifier="command_0x351c17"),
        ReturnSubroutine(),
    ]
)
