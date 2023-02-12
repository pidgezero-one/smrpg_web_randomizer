# referenced by ally_spells Psych Bomb

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 29, script = [
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=184, y=-20, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x35abd9"),
	Db(bytearray(b'\x83\x83')),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=184, y=116, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	SetAMEMToRandom(amem=0x60, upper_bound=9, identifier="command_0x35abec"),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x35ABF6),
	ClearAMEM16Bit(0x60),
	ReturnSubroutine()
])
