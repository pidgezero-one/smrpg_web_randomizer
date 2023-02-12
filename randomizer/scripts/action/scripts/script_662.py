#A0662_ROSE_TOWN_LIBERATED_WATER_GUY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	FaceSoutheast(),
	VisibilityOn(),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(2),
	SetSolidityBits(cant_walk_through=True),
	Walk1StepNortheast(),
	FaceSouthwest(),
	SetSequenceSpeed(SLOW),
	SetBit(TEMP_7043_7),
	Return()
])
