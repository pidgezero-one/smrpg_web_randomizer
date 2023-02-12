#A0663_ROSE_TOWN_LIBERATED_WATER_GUY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	Walk1StepSouthwest(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftNorthwestSteps(2),
	VisibilityOff(),
	TransferToXYZF(x=16, y=85, z=0, direction=EAST),
	SetBit(TEMP_7044_1),
	Return()
])
