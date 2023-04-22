"""Mute animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x358086"]),
        RunSubroutine(["command_0x358127"]),
        RunSubroutine(["command_0x358f10"]),
        ReturnSubroutine(),
    ]
)
