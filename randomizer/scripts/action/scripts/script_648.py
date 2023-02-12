#A0648_MOLEVILLE_WOMAN_NEAR_MOUNTAIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(4),
	EndLoop(),
	SetSequenceSpeed(NORMAL, identifier="ACTION_648_set_animation_speed_6"),
	StartLoopNTimes(3),
	ShiftZUpPixels(4),
	ShiftZDownPixels(4),
	EndLoop(),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_648_face_northwest_15"]),
	FaceSoutheast(),
	Jmp(["ACTION_648_set_animation_speed_16"]),
	FaceNorthwest(identifier="ACTION_648_face_northwest_15"),
	SetSequenceSpeed(VERY_FAST, identifier="ACTION_648_set_animation_speed_16"),
	Pause(32),
	FaceNortheast(),
	Jmp(["ACTION_648_set_animation_speed_6"]),
	Return()
])
