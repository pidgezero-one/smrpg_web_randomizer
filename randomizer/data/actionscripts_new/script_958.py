#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SetWalkingSpeed(speed=FASTEST),
	SetPriority(3),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	ShiftEastPixels(12, identifier="ACTION_958_shift_east_pixels_3"),
	SetWalkingSpeed(speed=SLOW),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	ShiftZDownSteps(4),
	ShiftZDownPixels(3),
	Pause(32),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True),
	Pause(11),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True),
	Pause(8),
	SetBit(TEMP_7044_0),
	ShiftZUpSteps(3),
	WalkToXYCoords(x=3, y=88),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastPixels(8),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownSteps(3),
	Pause(10),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True),
	Pause(10),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(16),
	ShiftZUpSteps(4),
	ShiftZUpPixels(3),
	WalkToXYCoords(x=1, y=72),
	Jmp(["ACTION_958_shift_east_pixels_3"])
])
