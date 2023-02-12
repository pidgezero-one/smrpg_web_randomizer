# referenced by monster_spells Flame, monster_spells Blast, monster_attacks Poison, monster_spells LightBeam, monster_attacks LullaBye, monster_attacks GetTough

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 45, script = [
	Pause1Frame(identifier="command_0x352576"),
	SetAMEM8BitToOMEMMain(amem=0x65, omem=0x65),
	JmpIfAMEM8BitNotEqualsConst(0x65, 1, ["command_0x352576"]),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68),
	IncAMEM8BitByConst(0x68, 1),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x68),
	IncAMEM8BitByConst(0x68, 1),
	SetOMEMMainToAMEM8Bit(omem=0x68, amem=0x68),
	ReturnSubroutine(),
	ClearAMEM8Bit(0x65),
	IncAMEM8BitByConst(0x65, 1),
	ReturnSubroutine(),
	SetAMEMToRandom(amem=0x60, upper_bound=25),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3525A3),
	ReturnSubroutine()
])
