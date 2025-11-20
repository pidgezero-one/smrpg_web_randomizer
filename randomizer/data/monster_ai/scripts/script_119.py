# 119 - LUMBLEREnemy

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
	Attack(Attack0, DoNothing, DoNothing),
	Wait1Turn(),
	Attack(Attack0, DoNothing, DoNothing),
	Wait1Turn(),
	CastSpell(CrystalSpell),
	Attack(DUMMYAttack13),
	Wait1Turn(),
	StartCounterCommands()
])