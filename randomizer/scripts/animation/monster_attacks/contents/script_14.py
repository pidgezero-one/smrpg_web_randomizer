"""Funguspike animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357d3e"]),
        RunSubroutine(["command_0x352f2f"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=15),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
