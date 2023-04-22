"""29 - Ameboid"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack2, ViroPlasm, PsychoPlasm),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        IfVarBitsClear(0x7EE000, [0]),
        SetVarBits(0x7EE000, [0]),
        CallTarget(MONSTER_2_CALL),
        CallTarget(MONSTER_3_CALL),
        CallTarget(MONSTER_4_CALL),
        CallTarget(MONSTER_5_CALL),
        Wait1TurnandRestartScript(),
    ]
)
