# 156 - GenoClone

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(FlameStone),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack89),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarBitsSet(0x7EE004, [0]),
        ClearVarBits(0x7EE00E, [1]),
        DecreaseVarBy1(0x7EE000),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        ClearVarBits(0x7EE00E, [0]),
        DecreaseVarBy1(0x7EE000),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        IfVarBitsSet(0x7EE004, [0]),
        ClearVarBits(0x7EE00E, [1]),
        DecreaseVarBy1(0x7EE000),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        ClearVarBits(0x7EE00E, [0]),
        DecreaseVarBy1(0x7EE000),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
