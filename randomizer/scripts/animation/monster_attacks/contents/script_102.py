"""PhysicalAttack116 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35313b"]),
        PlaySound(sound=S0009_ARROW_SLING),
        SetAMEM16BitToConst(0x60, 21),
        RunSubroutine(["command_0x352475"]),
        ReturnSubroutine(),
    ]
)
