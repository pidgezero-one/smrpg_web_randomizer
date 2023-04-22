"""2 - Skytroopa"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [Attack(AttackDoNothing, PhysicalAttack9, PhysicalAttack9), StartCounterCommands()]
)
