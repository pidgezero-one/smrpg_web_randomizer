"""200 - Belome2"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [7]),
        IfVarBitsSet(0x7EE004, [0]),
        SetVarBits(0x7EE004, [7]),
        RunBattleDialog(175),
        RunBattleEvent(BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS),
        RunBattleEvent(BE0060_BELOME_CLONES_SOMEONE),
        IncreaseVarBy1(0x7EE000),
        ClearVarBits(0x7EE004, [0]),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [0]),
        RunBattleEvent(BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS),
        RunBattleEvent(BE0060_BELOME_CLONES_SOMEONE),
        IncreaseVarBy1(0x7EE000),
        ClearVarBits(0x7EE004, [0]),
        Wait1TurnandRestartScript(),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(AuroraFlash, LightBeam, LightBeam),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack1, LullaBye),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleDialog(176),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        IfVarLessThan(0x7EE000, 2),
        SetVarBits(0x7EE004, [0]),
        Wait1TurnandRestartScript(),
    ]
)
