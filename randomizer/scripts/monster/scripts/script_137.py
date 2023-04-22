"""137 - DodoSolo"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, Multistrike, Multistrike),
        Wait1Turn(),
        Attack(PhysicalAttack1, FlutterHush, FlutterHush),
        Wait1Turn(),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleEvent(BE0078_DODO_FLUTTERS_AND_EXITS_BATTLE),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
