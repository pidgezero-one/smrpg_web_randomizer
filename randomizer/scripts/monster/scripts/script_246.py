"""246 - Booster"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        IfHPBelow(500, identifier="booster_hits_hard"),
        Attack(PhysicalAttack1, SpritzBomb, LocoExpress),
        Wait1TurnandRestartScript(),
        IfLastMonsterStanding(),
        Attack(PhysicalAttack1, PhysicalAttack25, PhysicalAttack1),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
    ]
)
