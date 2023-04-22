"""HP Rain animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x358127"]),
        RunSubroutine(["command_0x359174"]),
        ReturnSubroutine(),
    ]
)
