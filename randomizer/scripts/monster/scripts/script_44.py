"""44 - HeavyTroopa"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTurnCounterEquals(2),
        Attack(PhysicalAttack108),
        ClearVar(ATTACK_PHASE_COUNTER),
        Wait1TurnandRestartScript(),
        RunBattleDialog(210),
        StartCounterCommands(),
    ]
)
