"""188 - YaridovichMirage"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
        CastSpell(MeteorBlast, StaticE, Bolt),
        IncreaseVarBy1(0x7EE002),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1),
        IncreaseVarBy1(0x7EE002),
        StartCounterCommands(),
        IfHPBelow(0),
        ClearVar(0x7EE002),
        RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
        ClearVarBits(0x7EE000, [0]),
        ClearVarBits(0x7EE003, [0]),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
