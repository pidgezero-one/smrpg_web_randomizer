# 49 - Frogog

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        SetTarget(RANDOM_OPPONENT),
        Attack(PhysicalAttack1),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack40, PhysicalAttack40),
        StartCounterCommands(),
    ]
)
