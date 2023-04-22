"""FearRoulette animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x352523"]),
        RunSubroutine(["command_0x357bef"]),
        PlaySound(sound=S0012_BOMB_EXPLOSION),
        VisibilityOff(),
        SetAMEM16BitToConst(0x60, 11),
        RunSubroutine(["command_0x352489"]),
        RunSubroutine(["command_0x3523c4"]),
        Db(bytearray(b"Z")),
        ReturnSubroutine(),
    ]
)
