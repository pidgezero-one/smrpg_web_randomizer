"""9 - Goby"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [0]),
        ClearVarBits(0x7EE003, [0]),
        RunBattleDialog(128),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack9, PhysicalAttack9, PhysicalAttack9),
        StartCounterCommands(),
        IfTargetedByElement([Element.THUNDER]),
        SetVarBits(0x7EE003, [0]),
        Wait1TurnandRestartScript(),
    ]
)
