"""66 - Malakoopa"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(BOWSER),
        RunBattleDialog(130),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarBitsClear(0x7EE004, [0]),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
        SetVarBits(0x7EE004, [0]),
        RunBattleDialog(129),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [0]),
        IfLastMonsterStanding(),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [0]),
        SetTarget(RANDOM_ALLY_EXCLUDING_SELF_OPPONENT_IF_SOLO),
        Attack(PhysicalAttack0),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack9, PhysicalAttack9, AttackDoNothing),
        StartCounterCommands(),
    ]
)
