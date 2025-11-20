# 126 - MASTABLASTAEnemy

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
	IfHPBelow(512),
	CastSpell(CrystalSpell, BlastSpell, StormSpell),
	Wait1TurnandRestartScript(),
	Attack(Attack0, Attack0, EerieJigAttack),
	StartCounterCommands()
])