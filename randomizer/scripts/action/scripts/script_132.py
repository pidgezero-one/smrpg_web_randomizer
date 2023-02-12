#A0132_HENCHMAN_BONKING_HOUSE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_132_set_priority_0"),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x07\xa0\xff')),
	SetWalkingSpeed(SLOW),
	ShiftNorthwestPixels(16),
	BPL262728(),
	FaceSoutheast(),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x04\xa0\xff')),
	ShiftSoutheastPixels(16),
	BPL262728(),
	Jmp(["ACTION_132_set_priority_0"])
])
