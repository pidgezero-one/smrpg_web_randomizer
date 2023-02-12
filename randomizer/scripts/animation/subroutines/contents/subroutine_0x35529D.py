# referenced by monster_attacks PhysicalAttack40

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 40, script = [
	RunSubroutine(["command_0x353437"], identifier="queuestart_0x35529d"),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x67),
	ClearAMEM8Bit(0x66),
	PlaySound(sound=S0021_SCARECROW_BIRDIES),
	SetAMEM16BitToConst(0x60, 11),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35624B),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x35624B),
	RunSubroutine(["command_0x3533df"]),
	RunSubroutine(["command_0x3533ea"]),
	Jmp(["command_0x35252f"])
])
