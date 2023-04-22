"""222 - Domino"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
        Attack(Endobubble),
        Wait1TurnandRestartScript(),
        CastSpell(FlameStone, LightningOrb, Blizzard),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RunBattleEvent(BE0054_CLOAKER_TEAMS_UP_WITH_EARTHLINK),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
