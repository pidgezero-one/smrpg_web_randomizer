"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        RunSubroutine(["command_0x35303b"]),
        RunSubroutine(["command_0x35788e"]),
        RunBattleEvent(script_id=BE0070_JINX_USES_JINXED),
        RunSubroutine(["command_0x3535ad"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
