"""150 - WaterCrystal"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfCurrentlyInFormationID(350),
        IfTargetKOed(MONSTER_1_CALL),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(Crystal, DiamondSaw, IceRock),
        Wait1TurnandRestartScript(),
        CastSpell(Blizzard, Blizzard, Solidify),
        StartCounterCommands(),
    ]
)
