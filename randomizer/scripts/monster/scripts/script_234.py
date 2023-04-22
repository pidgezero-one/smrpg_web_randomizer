"""234 - Smithy1"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        RunBattleEvent(BE0096_NOTHING),
        CastSpell(Sledge),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE003, [0]),
        ClearVarBits(0x7EE003, [0]),
        CastSpell(Sledge),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(MeteorSwarm, MeteorSwarm, MegaDrain),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack93),
        StartCounterCommands(),
        IfHPBelow(0),
        IfTargetAlive(MONSTER_4_SET),
        RunBattleEvent(BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC),
        RemoveTarget(MONSTER_4_SET),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        RunBattleEvent(BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
