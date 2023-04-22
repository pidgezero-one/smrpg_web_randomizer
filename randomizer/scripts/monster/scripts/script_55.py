"""55 - Stumpet"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTurnCounterEquals(2),
        Attack(Backfire, VaVaVoom, Backfire),
        ClearVar(ATTACK_PHASE_COUNTER),
        Wait1TurnandRestartScript(),
        DoMonsterBehaviour(4),
        RunBattleDialog(213),
        StartCounterCommands(),
    ]
)
