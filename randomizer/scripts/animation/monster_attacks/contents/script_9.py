"""PhysicalAttack11 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x353005"]),
        RunSubroutine(["command_0x3579a2"]),
        RunSubroutine(["command_0x352f2f"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=15),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x357a03"]),
        ReturnSubroutine(),
    ]
)
