"""10 - Bloober"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack8, PhysicalAttack8, InkBlast),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
    ]
)
