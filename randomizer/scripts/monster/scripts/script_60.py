"""60 - Carriboscis"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack11, PhysicalAttack11, ScrowBell),
        Wait1Turn(),
        Attack(SporeChimes, ScrowBell, DoomReverb),
        Wait1Turn(),
        Attack(PhysicalAttack11, PhysicalAttack11, SporeChimes),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
