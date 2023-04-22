"""16 - K9"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, Fangs, Fangs),
        Wait1Turn(),
        Attack(PhysicalAttack1, Howl, Howl),
        StartCounterCommands(),
    ]
)
