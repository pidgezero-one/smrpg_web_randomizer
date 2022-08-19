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
	SetWalkingSpeed(speed=FAST),
	ShiftZDownSteps(9),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(speed=NORMAL),
	WalkToXYCoords(x=5, y=75),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpSteps(9),
	SetWalkingSpeed(speed=NORMAL),
	FaceNortheast(),
	SetSolidityBits(cant_pass_walls=True),
	WalkToXYCoords(x=25, y=35),
	Jmp(["ACTION_285_face_southwest_11"])
])
