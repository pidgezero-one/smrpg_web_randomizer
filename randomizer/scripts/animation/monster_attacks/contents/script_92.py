"""Gnight animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        SetAMEM8BitTo7E1x(0x6E, 0x7EE00E),
        JmpIfAMEM8BitEqualsConst(0x6E, 1, ["command_0x351df6"]),
        JmpIfAMEM8BitEqualsConst(0x6E, 2, ["command_0x351dfd"]),
        RunBattleEvent(script_id=BE0085_FEAR_ROULETTE, offset=4),
        Jmp(["command_0x351e01"]),
        RunBattleEvent(
            script_id=BE0085_FEAR_ROULETTE, offset=2, identifier="command_0x351df6"
        ),
        Jmp(["command_0x351e01"]),
        RunBattleEvent(script_id=BE0085_FEAR_ROULETTE, identifier="command_0x351dfd"),
        ResetSpriteSequence(identifier="command_0x351e01"),
        AttackTimerBegins(),
        ReturnSubroutine(),
    ]
)
