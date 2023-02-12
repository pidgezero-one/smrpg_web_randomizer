#A0658_PIPE_VAULT_THWOMP_ROOM_SHAKE_CAMERA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(FASTEST),
	ShiftSouthPixels(8),
	SetBit(TEMP_7043_2),
	ShiftNorthPixels(16),
	ShiftSouthPixels(16),
	ShiftNorthPixels(12),
	ShiftSouthPixels(8),
	ClearBit(TEMP_7043_2),
	ShiftNorthPixels(8),
	ShiftSouthPixels(6),
	ShiftNorthPixels(4),
	ShiftSouthPixels(4),
	ShiftNorthPixels(2),
	Return()
])
