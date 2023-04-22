"""PhysicalAttack105 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        RunSubroutine(["command_0x3531df"]),
        SetAMEM16BitToConst(0x60, 0),
        RunSubroutine(["command_0x35247f"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"]),
        ReturnSubroutine(),
    ]
)
