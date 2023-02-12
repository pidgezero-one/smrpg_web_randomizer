# referenced by monster_attacks PhysicalAttack7

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 53, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x35600c"),
	SetAMEM8BitToConst(0x61, 129),
	SetAMEM8BitToConst(0x62, 32),
	Db(bytearray(b' \x83\x01\x00')),
	SetAMEM8BitToConst(0x64, 1),
	SetAMEM8BitToConst(0x65, 0),
	SetAMEM8BitToConst(0x66, 8),
	SetAMEM16BitToConst(0x67, 25088),
	SetAMEM16BitToConst(0x6E, 65535),
	SetAMEMToAMEM16Bit(dest_amem=0x6C, amem=0x6E),
	EnableSpritesOnSubscreen(),
	Db(bytearray(b'\x17')),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=6),
	RemoveObject(),
	DisableSpritesOnSubscreen(),
	ReturnObjectQueue()
])
