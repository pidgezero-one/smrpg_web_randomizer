"""253 - Domino2"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE004, [0]),
        DoMonsterBehaviour(28),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(DiamondSaw, LightBeam, IceRock),
        Wait1TurnandRestartScript(),
        CastSpell(Blizzard, Solidify, Bolt),
        StartCounterCommands(),
        IfHPBelow(0),
        SetVarBits(0x7EE004, [0]),
        DoMonsterBehaviour(28),
        SetUntargetable(SELF),
        Wait1TurnandRestartScript(),
    ]
)
