"""105 - Juju"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTurnCounterEquals(4),
        SetTarget(ALL_OPPONENTS),
        CastSpell(KnockOut),
        ClearVar(ATTACK_PHASE_COUNTER),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack0, PhysicalAttack0, MushFunk),
        Wait1Turn(),
        Attack(PhysicalAttack0, PhysicalAttack0, Scream),
        Wait1Turn(),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        Attack(AttackDoNothing, AttackDoNothing, SilverBullet),
        Wait1TurnandRestartScript(),
    ]
)
