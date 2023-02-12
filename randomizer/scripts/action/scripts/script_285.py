#A0285_KEEP_BULLET_BILL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	Pause(100),
	SetPriority(3),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65512),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(180),
	EndLoop(),
	TransferToXYZF(x=25, y=35, z=19, direction=EAST),
	VisibilityOn(),
	FaceSouthwest(identifier="ACTION_285_face_southwest_11"),
	SetWalkingSpeed(FAST),
	ShiftZDownSteps(9),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(NORMAL),
	WalkToXYCoords(x=5, y=75),
	SetWalkingSpeed(FAST),
	ShiftZUpSteps(9),
	SetWalkingSpeed(NORMAL),
	FaceNortheast(),
	SetSolidityBits(cant_pass_walls=True),
	WalkToXYCoords(x=25, y=35),
	Jmp(["ACTION_285_face_southwest_11"])
])
