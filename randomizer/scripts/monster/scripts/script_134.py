"""134 - BoxBoy"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        DoMonsterBehaviour(7),
        CallTarget(MONSTER_2_CALL),
        RunBattleDialog(216),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack0, CarniKiss, Scream),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        CastSpell(WaterBlast, Blast, Blast),
        Wait1TurnandRestartScript(),
    ]
)
