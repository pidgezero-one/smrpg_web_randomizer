"""186 - Grit"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        SetTarget(RANDOM_OPPONENT),
        Wait1Turn(),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack101),
        RemoveTarget(SELF),
        StartCounterCommands(),
        IfTargetAlive(SELF),
        Wait1TurnandRestartScript(),
        RemoveTarget(MONSTER_1_SET),
    ]
)
