"""125 - Crippo"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        SetTarget(RANDOM_OPPONENT),
        CastSpell(LightningOrb),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(Thornet),
        SetVarBits(0x7EE004, [0]),
        Wait1TurnandRestartScript(),
        SetTarget(RANDOM_OPPONENT),
        Attack(PhysicalAttack0, DoomReverb, Vigorup),
        Wait1Turn(),
        Attack(PhysicalAttack0),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
