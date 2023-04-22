"""146 - MachineMadeDrillBit"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, Skewer, PhysicalAttack1),
        StartCounterCommands(),
        IfCurrentlyInFormationID(361),
        IfTargetKOed(AT_LEAST_ONE_ALLY),
        IncreaseVarBy1(0x7EE007),
        IfVarEqualOrGreaterThan(0x7EE007, 4),
        ClearVar(0x7EE007),
        ClearVar(0x7EE003),
        SetTargetable(MONSTER_1_SET),
        ClearVarBits(0x7EE000, [1]),
        RunBattleEvent(BE0025_DRILL_BIT),
        Wait1TurnandRestartScript(),
    ]
)
