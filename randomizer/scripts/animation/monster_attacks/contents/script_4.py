"""PhysicalAttack6 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x352fea"]),
        RunSubroutine(["command_0x3577e2"]),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x3515e8"]),
        RunSubroutine(["command_0x353140"]),
        Jmp(["command_0x3515fa"]),
        SpriteSequence(sequence=3, identifier="command_0x3515e8"),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        PlaySound(sound=S0146_SLAP),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        PlaySound(sound=S0146_SLAP),
        PauseScriptUntilSpriteSequenceDone(),
        ResetSpriteSequence(),
        PlaySound(sound=S0025_SLAP_BIG),
        RunSubroutine(["command_0x3523c4"], identifier="command_0x3515fa"),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
