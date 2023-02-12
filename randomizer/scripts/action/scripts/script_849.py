#A0849_BEAN_VALLEY_BEANSTALK_BRICK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(2, identifier="ACTION_849_pause_0"),
	ShiftZDownPixels(1),
	Pause(4),
	ShiftZDownPixels(1),
	Pause(13),
	ShiftZUpPixels(1),
	Pause(4),
	ShiftZUpPixels(1),
	Pause(2),
	ShiftZUpPixels(1),
	Pause(4),
	ShiftZUpPixels(1),
	Pause(13),
	ShiftZDownPixels(1),
	Pause(4),
	ShiftZDownPixels(1),
	JmpIfBitSet(TEMP_708C_4, ["ACTION_849_ret_18"]),
	Jmp(["ACTION_849_pause_0"]),
	Return(identifier="ACTION_849_ret_18")
])
