"""PhysicalAttack20 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SpriteSequence(sequence=5, looping_on=True),
        RunSubroutine(["command_0x3577e2"]),
        RunSubroutine(["command_0x353140"]),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
