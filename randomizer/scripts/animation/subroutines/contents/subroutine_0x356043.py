# referenced by monster_attacks PhysicalAttack10, monster_spells WillyWisp

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 28, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=-8, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x356043"),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 7),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35624B),
	RunSubroutine(["command_0x352552"]),
	SetOMEMMainToAMEM8Bit(omem=0x68, amem=0x68),
	ReturnObjectQueue()
])
