# 249 - Johnny

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE004, [0]),
        IfVarBitsClear(0x7EE004, [1]),
        IfLastMonsterStanding(),
        IfTargetAlive(SLOT_3),
        SetVarBits(0x7EE004, [1]),
        SetTarget(RANDOM_OPPONENT),
        RunBattleEvent(BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE),
        SetUntargetable(MONSTER_2_SET),
        SetUntargetable(MONSTER_3_SET),
        Wait1TurnandRestartScript(),
        IfLastMonsterStanding(),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Attack(PhysicalAttack1, Skewer, Skewer),
        Wait1TurnandRestartScript(),
        IfLastMonsterStanding(),
        CastSpell(SpellDoNothing, DiamondSaw, MegaDrain),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1),
        StartCounterCommands(),
        IfHPBelow(0),
        IncreaseVarBy1(0x7EE003),
        DoMonsterBehaviour(3),
        RemoveTarget(ALL_ALLIES_AND_SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(400, identifier="johnny_def"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(GetTough),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
    ]
)
