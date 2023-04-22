"""185 - ShyGuyHenchman"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        Attack(PhysicalAttack107, PhysicalAttack107, DoomReverb),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack107),
        Wait1Turn(),
        Attack(PhysicalAttack107, PhysicalAttack107, LullaBye),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
