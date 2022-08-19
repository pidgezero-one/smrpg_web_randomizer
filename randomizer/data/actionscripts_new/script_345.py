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
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_345_set_animation_speed_0"),
	Inc(TEMP_702C),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_700C),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_345_shift_f_direction_steps_6"]),
	SetWalkingSpeed(speed=NORMAL),
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
