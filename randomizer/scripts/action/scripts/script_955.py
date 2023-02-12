#A0955_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	WalkToXYCoords(x=7, y=75),
	ShiftNortheastPixels(11),
	Db(bytearray(b' \x03')),
	Db(bytearray(b'$\xc0\x01\xa0\x02')),
	Pause(5),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	BPL262728(),
	ShiftSoutheastSteps(16),
	ShiftToXYCoords(x=8, y=35),
	ShiftSoutheastSteps(5),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	Jmp(["ACTION_953_set_animation_speed_0"])
])
