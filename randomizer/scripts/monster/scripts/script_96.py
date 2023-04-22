"""96 - Starcruster"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack0),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(PhysicalAttack51),
        Wait1TurnandRestartScript(),
    ]
)
