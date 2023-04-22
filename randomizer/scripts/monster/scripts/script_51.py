"""51 - Gunyolk"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTurnCounterEquals(2),
        ClearVar(ATTACK_PHASE_COUNTER),
        CastSpell(BreakerBeam),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack0, PhysicalAttack0, Echofinder),
        ClearVarBits(0x7EE00F, [0]),
        Wait1TurnandRestartScript(),
        CastSpell(MegaDrain, MegaDrain, Electroshock),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
