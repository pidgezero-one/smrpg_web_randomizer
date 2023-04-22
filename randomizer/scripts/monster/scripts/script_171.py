"""171 - BahamuttChester"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
        CastSpell(FlameWall, Flame, Drain),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack3, IronMaiden, PhysicalAttack27),
        StartCounterCommands(),
        IfHPBelow(0),
        IfCurrentlyInFormationID(357),
        ClearVar(0x7EE000),
        SetTargetable(MONSTER_1_SET),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
