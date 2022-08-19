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
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(4),
	EndLoop(),
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_648_set_animation_speed_6"),
	StartLoopNTimes(3),
	ShiftZUpPixels(4),
	ShiftZDownPixels(4),
	EndLoop(),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_648_face_northwest_15"]),
	FaceSoutheast(),
	Jmp(["ACTION_648_set_animation_speed_16"]),
	FaceNorthwest(identifier="ACTION_648_face_northwest_15"),
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_648_set_animation_speed_16"),
	Pause(32),
	FaceNortheast(),
	Jmp(["ACTION_648_set_animation_speed_6"]),
	Return()
])
