"""23 - Pandorite"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        CastSpell(FlameWall, Flame, FlameWall),
        Wait1Turn(),
        Attack(PhysicalAttack0, CarniKiss, Scream),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
