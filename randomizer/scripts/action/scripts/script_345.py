#A0345_SHIP_1ST_WATER_ROOM_FISH

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_345_set_animation_speed_0"),
	Inc(TEMP_702C),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_700C),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_345_shift_f_direction_steps_6"]),
	SetWalkingSpeed(NORMAL),
	ShiftFDirectionSteps(2, identifier="ACTION_345_shift_f_direction_steps_6"),
	Inc(TEMP_702C),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_700C),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_345_face_mario_13"]),
	TurnRandomDirection(),
	Jmp(["ACTION_345_set_animation_speed_0"]),
	FaceMario(identifier="ACTION_345_face_mario_13"),
	Jmp(["ACTION_345_set_animation_speed_0"])
])
