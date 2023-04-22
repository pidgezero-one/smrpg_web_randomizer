"""255 - Culex"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        RunBattleDialog(215),
        RunBattleEvent(BE0074_CULEX_SUMMONS_CRYSTALS),
        Wait1TurnandRestartScript(),
        IfTurnCounterEquals(3),
        ClearVar(ATTACK_PHASE_COUNTER),
        CastSpell(Shredder),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(FlameStone, DarkStar, MeteorBlast),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack0),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
