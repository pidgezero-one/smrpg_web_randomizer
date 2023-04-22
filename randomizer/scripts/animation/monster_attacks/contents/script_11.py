"""PhysicalAttack15 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        PlaySound(sound=S0087_BIG_BOUNCE),
        RunSubroutine(["command_0x357a77"]),
        RunSubroutine(["command_0x35313b"]),
        PlaySound(sound=S0164_CARROBOSCIS_ATTACK),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x357878"]),
        ReturnSubroutine(),
    ]
)
