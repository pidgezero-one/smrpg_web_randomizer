"""Bowser Crush animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x358086"]),
        RunSubroutine(["command_0x358fc4"]),
        ReturnSubroutine(),
    ]
)
