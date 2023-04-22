"""145 - MachineMadeShyster"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack13),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(SpellDoNothing, Drain, Drain),
        StartCounterCommands(),
        IfTargetKOed(AT_LEAST_ONE_ALLY),
        IncreaseVarBy1(0x7EE000),
        IfVarEqualOrGreaterThan(0x7EE000, 4),
        ClearVarBits(0x7EE003, [0]),
        IfVarBitsSet(0x7EE003, [7]),
        ClearVarBits(0x7EE003, [7]),
        SetTargetable(MONSTER_1_SET),
        RunBattleEvent(BE0005_MACK_RETURNS_TO_BATTLE),
        Wait1TurnandRestartScript(),
    ]
)
