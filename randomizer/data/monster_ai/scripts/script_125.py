# 125 - CRIPPOEnemy
# pyright: reportWildcardImportFromLibrary=false

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
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	SetTarget(RANDOM_OPPONENT),
	CastSpell(LightningOrbSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE004, [0]),
	SetTarget(SELF),
	Attack(ThornetAttack),
	SetVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	SetTarget(RANDOM_OPPONENT),
	Attack(Attack0, DoomReverbAttack, VigorupAttack),
	Wait1Turn(),
	Attack(Attack0),
	Wait1Turn(),
	StartCounterCommands()
])