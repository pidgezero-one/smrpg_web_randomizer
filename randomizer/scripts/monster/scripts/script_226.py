# 226 - Yaridovich

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE003, [0]),
        CastSpell(WaterBlast),
        SetVarBits(0x7EE003, [0]),
        Wait1TurnandRestartScript(),
        IfVarEqualOrGreaterThan(0x7EE002, 3),
        IfVarBitsSet(0x7EE000, [0]),
        ClearVarBits(0x7EE000, [0]),
        ClearVar(0x7EE002),
        ClearVarBits(0x7EE003, [0]),
        RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
        RemoveTarget(MONSTER_2_SET),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE000, [0]),
        Attack(PhysicalAttack1, Pierce, PhysicalAttack31),
        Wait1TurnandRestartScript(),
        IfVarLessThan(0x7EE001, 2),
        CastSpell(FlameStone, WillyWisp, WaterBlast),
        IncreaseVarBy1(0x7EE001),
        Wait1TurnandRestartScript(),
        ClearVar(0x7EE001),
        SetVarBits(0x7EE000, [0]),
        RunBattleDialog(133),
        RunBattleEvent(BE0022_YARIDOVICH_MIRAGE_ATTACK),
        StartCounterCommands(),
        IfHPBelow(0),
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
        RemoveTarget(MONSTER_2_SET),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
