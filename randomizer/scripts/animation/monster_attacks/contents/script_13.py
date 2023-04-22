"""PhysicalAttack18 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        PlaySound(sound=S0097_PLASMA_TOSS),
        RunSubroutine(["command_0x357d0b"]),
        RunSubroutine(["command_0x352f2f"]),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x35789e"]),
        ReturnSubroutine(),
    ]
)
