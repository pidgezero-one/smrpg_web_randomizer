#A0154_TADPOLE_POND_TADPOLE_DEFAULT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FixedFCoordOn(identifier="ACTION_154_fixed_f_coord_on_0"),
	SetSequenceSpeed(FAST),
	SequenceLoopingOn(),
	SetWalkingSpeed(SLOW),
	ShiftWestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNorthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSoutheastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSouthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftWestPixels(1),
	Pause(1),
	Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
