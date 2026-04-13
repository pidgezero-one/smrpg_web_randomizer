# 254 - CANDLEEnemy
# pyright: reportWildcardImportFromLibrary=false

from randomizer.data.packs.pack_collection import FORM0137_ONE_BUNDT2_ONE_RASPBERRY2_TWO_TORTE2_ONE_CANDLE, FORM0286_ONE_BUNDT_ONE_RASPBERRY_TWO_TORTE
from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing
from ...variables.battle_event_names import *
from ...variables.battle_variable_names import *
from ...items.items import *
from ...spells.spells import *
from ...enemies.enemies import *
from ...enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *

script = MonsterScript([
    IfCurrentlyInFormationID(286),
	IfTurnCounterEquals(3),
	SetTargetable(SELF),
	ClearVar(BV7EE006_ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
    IfCurrentlyInFormationID(137),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript(),
    
	StartCounterCommands(),
    IfCurrentlyInFormationID(286),
	IfTargetedByRegularAttack(),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript(),
    IfCurrentlyInFormationID(137),
	IfTargetedByRegularAttack(),
	Wait1TurnandRestartScript(),
])