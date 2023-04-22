"""140 - CorkpediteBody"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(MONSTER_1_SET),
        Wait1TurnandRestartScript(),
        Attack(Migraine),
        RemoveTarget(SELF),
        StartCounterCommands(),
    ]
)
