"""87 - Hidon"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        DoMonsterBehaviour(7),
        CallTarget(MONSTER_2_CALL),
        CallTarget(MONSTER_3_CALL),
        CallTarget(MONSTER_4_CALL),
        CallTarget(MONSTER_5_CALL),
        RunBattleDialog(216),
        Wait1TurnandRestartScript(),
        CastSpell(StaticE, WillyWisp, FlameStone),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(PhysicalAttack0, CarniKiss, PhysicalAttack0),
        Wait1TurnandRestartScript(),
    ]
)
