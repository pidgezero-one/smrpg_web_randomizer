#A0953_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_BASE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_953_set_animation_speed_0"),
	ShiftToXYCoords(x=3, y=70),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	ShiftNorthSteps(2),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	Db(bytearray(b' \x03')),
	Db(bytearray(b'$\x00\x01P\x01')),
	Pause(48),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	Pause(32),
	BPL262728(),
	Pause(8),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	ShiftNortheastSteps(4),
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
	Jmp(["ACTION_953_set_animation_speed_0"])
])
