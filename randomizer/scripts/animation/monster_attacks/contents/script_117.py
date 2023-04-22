"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x352fa6"]),
        RunSubroutine(["command_0x357f5e"]),
        PlaySound(sound=S0012_BOMB_EXPLOSION),
        VisibilityOff(),
        RunSubroutine(["command_0x3523df"]),
        RunSubroutine(["command_0x357f1e"]),
        ReturnSubroutine(),
    ]
)
