"""1 - Spikey"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        SetTarget(RANDOM_OPPONENT),
        Attack(AttackDoNothing, PhysicalAttack3, PhysicalAttack3),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack16),
        StartCounterCommands(),
    ]
)
