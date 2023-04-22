"""PhysicalAttack4 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357808"]),
        RunSubroutine(["command_0x353140"]),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x357878"]),
        ReturnSubroutine(),
    ]
)
