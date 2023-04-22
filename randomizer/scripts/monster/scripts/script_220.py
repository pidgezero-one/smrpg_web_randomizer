"""220 - CzarDragon"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(WaterBlast, FlameWall, FlameWall),
        Wait1TurnandRestartScript(),
        IfLastMonsterStanding(),
        Attack(PhysicalAttack1, PhysicalAttack1, IronMaiden),
        IfTargetAlive(AT_LEAST_ONE_OPPONENT),
        RunBattleEvent(BE0046_CZAR_DRAGON_SUMMONS_HELIOS),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(0),
        IfLastMonsterStanding(),
        RunBattleEvent(BE0044_CZAR_DRAGON_DIES),
        CallTarget(MONSTER_2_CALL),
        DoMonsterBehaviour(2),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
        RunBattleEvent(BE0044_CZAR_DRAGON_DIES),
        CallTarget(MONSTER_2_CALL),
        DoMonsterBehaviour(2),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
