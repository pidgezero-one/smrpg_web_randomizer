# 39 - BABAYAGAEnemy
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
	IfVarBitsSet(BV7EE004, [0]),
	SetTarget(SELF),
	Attack(ThornetAttack),
	ClearVarBits(BV7EE004, [0]),
	SetVarBits(BV7EE004, [1]),
	Wait1TurnandRestartScript(),
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	Attack(Attack1, Attack1, VenomDroolAttack),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [1]),
	CastSpell(SandStormSpell, MegaRecoverSpell, SandStormSpell),
	Wait1TurnandRestartScript(),
	SetVarBits(BV7EE004, [0]),
	Attack(Attack1),
	StartCounterCommands()
])