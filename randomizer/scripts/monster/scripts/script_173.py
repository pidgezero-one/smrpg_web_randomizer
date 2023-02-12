# 173 - MachineMadeAxemBlackHenchman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack5, PhysicalAttack5, PhysicalAttack25),
        IfTargetAlive(AT_LEAST_ONE_OPPONENT),
        Attack(PhysicalAttack5, PhysicalAttack5, PhysicalAttack25),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        Attack(SpritzBomb),
        Wait1TurnandRestartScript(),
    ]
)
