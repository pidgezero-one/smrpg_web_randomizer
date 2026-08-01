# 174 - CULEX3DEnemy

from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from ...variables.battle_event_names import *
from ...variables.battle_variable_names import *
from ...items.items import *
from ...spells.spells import *
from ...enemies.enemies import *
from ...enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *

# Countdown phase is tracked in BV7EE001 bits 1-4, NOT by script pointer position.
# The crystals revive Culex with CallTarget (script_183/185/203/242), and CallTarget's
# worker at $C2/C641 zeroes $7E0052/53 - the monster's AI script offset. Any positional
# phase state is therefore destroyed on every revival. Every block ends with
# Wait1TurnandRestartScript() so each turn re-dispatches from the top.

script = MonsterScript([
	# Intro - once per battle
	IfVarBitsClear(BV7EE001, [0]),
	RunBattleEvent(BE0077_CULEX_3D),
	Attack(CULEXTURNSAttack),
	SetTarget(AT_LEAST_ONE_OPPONENT),
	Attack(MeteorAttack),
	SetTarget(AT_LEAST_ONE_OPPONENT),
	Attack(Attack11),
	SetVarBits(BV7EE001, [0]),
	Wait1TurnandRestartScript(),

	# "4"
	IfVarBitsClear(BV7EE001, [1]),
	Attack(CULEXTURNSAttack),
	RunBattleDialog(139),
	CastSpell(FlameStoneSpell, MeteorBlastSpell, DarkStarSpell),
	SetVarBits(BV7EE001, [1]),
	Wait1TurnandRestartScript(),

	# "3"
	IfVarBitsClear(BV7EE001, [2]),
	Attack(CULEXTURNSAttack),
	RunBattleDialog(140),
	CastSpell(ShredderSpell),
	SetVarBits(BV7EE001, [2]),
	Wait1TurnandRestartScript(),

	# "Commands restored!" + "2"
	IfVarBitsClear(BV7EE001, [3]),
	Attack(CULEXTURNSAttack),
	RunBattleDialog(148),
	EnableCommand([COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]),
	ClearVar(BV7EE006_ATTACK_PHASE_COUNTER),
	ClearVarBits(BV7EE002, [0]),
	RunBattleDialog(141),
	Attack(Attack0),
	SetVarBits(BV7EE001, [3]),
	Wait1TurnandRestartScript(),

	# "1"
	IfVarBitsClear(BV7EE001, [4]),
	Attack(CULEXTURNSAttack),
	RunBattleDialog(142),
	CastSpell(FlameStoneSpell, MeteorBlastSpell, DarkStarSpell),
	SetVarBits(BV7EE001, [4]),
	Wait1TurnandRestartScript(),

	# "0" - alone: Final Claw. Countdown restarts.
	IfLastMonsterStanding(),
	Attack(CULEXTURNSAttack),
	RunBattleDialog(143),
	Attack(FinalClawAttack),
	ClearVarBits(BV7EE001, [1, 2, 3, 4]),
	Wait1TurnandRestartScript(),

	# "0" - crystals still up: Meteor. Countdown restarts.
	Attack(CULEXTURNSAttack),
	RunBattleDialog(143),
	SetTarget(AT_LEAST_ONE_OPPONENT),
	Attack(MeteorAttack),
	SetTarget(AT_LEAST_ONE_OPPONENT),
	Attack(Attack11),
	ClearVarBits(BV7EE001, [1, 2, 3, 4]),
	Wait1TurnandRestartScript(),

	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
