"""Ultra Flame animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3580cb"]),
        RunSubroutine(["command_0x358127"]),
        RunSubroutine(["command_0x358de8"]),
        ReturnSubroutine(),
    ]
)
