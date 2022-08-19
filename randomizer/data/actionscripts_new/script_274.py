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
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_274_set_animation_speed_0"),
	SequenceLoopingOn(),
	JmpIfBitSet(TEMP_7076_0, ["ACTION_274_sequence_looping_off_63"]),
	Set700CToObjectCoord(object=MARIO, coord=X, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	DecVarFrom700C(TEMP_7028),
	AddConstToVar(PRIMARY_TEMP_700C, 256),
	CompareVarToConst(PRIMARY_TEMP_700C, 128),
	JmpIfComparisonResultIsLesser(["ACTION_274_set_700C_to_object_coord_13"]),
	CompareVarToConst(PRIMARY_TEMP_700C, 384),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_274_set_700C_to_object_coord_13"]),
	Jmp(["ACTION_274_shift_f_direction_pixels_24"]),
	Set700CToObjectCoord(object=MARIO, coord=Y, pixel=True, identifier="ACTION_274_set_700C_to_object_coord_13"),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True),
	DecVarFrom700C(TEMP_7028),
	AddConstToVar(PRIMARY_TEMP_700C, 256),
	CompareVarToConst(PRIMARY_TEMP_700C, 64),
	JmpIfComparisonResultIsLesser(["ACTION_274_face_mario_23"]),
	CompareVarToConst(PRIMARY_TEMP_700C, 320),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_274_face_mario_23"]),
	Jmp(["ACTION_274_shift_f_direction_pixels_24"]),
	FaceMario(identifier="ACTION_274_face_mario_23"),
	ShiftFDirectionPixels(1, identifier="ACTION_274_shift_f_direction_pixels_24"),
	Set700CToObjectCoord(object=MARIO, coord=Z, pixel=True, identifier="ACTION_274_set_700C_to_object_coord_25"),
	AddConstToVar(PRIMARY_TEMP_700C, 192),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Z, pixel=True),
	DecVarFrom700C(TEMP_7028),
	JmpIfLoadedMemoryIs0(["ACTION_274_pause_33"]),
	JmpIfLoadedMemoryIsBelow0(["ACTION_274_shift_z_down_pixels_35"]),
	JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_274_shift_z_up_pixels_37"]),
	Pause(1, identifier="ACTION_274_pause_33"),
	Jmp(["ACTION_274_pause_38"]),
	ShiftZDownPixels(1, identifier="ACTION_274_shift_z_down_pixels_35"),
	Jmp(["ACTION_274_pause_38"]),
	ShiftZUpPixels(1, identifier="ACTION_274_shift_z_up_pixels_37"),
	Pause(2, identifier="ACTION_274_pause_38"),
	JmpIfBitSet(TEMP_7076_0, ["ACTION_274_sequence_looping_off_63"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
	FaceMario(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	DecVarFrom700C(TEMP_7028),
	Mem700CAndConst(0x0007),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_274_set_700C_to_object_coord_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_274_set_700C_to_object_coord_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_274_set_700C_to_object_coord_53"]),
	Jmp(["ACTION_274_set_animation_speed_0"]),
	Set700CToObjectCoord(object=MARIO, coord=F, pixel=True, identifier="ACTION_274_set_700C_to_object_coord_53"),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	DecVarFrom700C(TEMP_7028),
	Mem700CAndConst(0x0007),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_274_sequence_looping_off_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_274_sequence_looping_off_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_274_sequence_looping_off_63"]),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=80, tiles=0, destinations=["ACTION_274_set_700C_to_object_coord_25"]),
	Jmp(["ACTION_274_set_animation_speed_0"]),
	SequenceLoopingOff(identifier="ACTION_274_sequence_looping_off_63"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_274_set_sprite_sequence_70"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_274_set_sprite_sequence_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_274_set_sprite_sequence_74"]),
	SetSpriteSequence(index=9, looping_off=True, mirror_sprite=True),
	Jmp(["ACTION_274_pause_38"]),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True, identifier="ACTION_274_set_sprite_sequence_70"),
	Jmp(["ACTION_274_pause_38"]),
	SetSpriteSequence(index=8, looping_off=True, identifier="ACTION_274_set_sprite_sequence_72"),
	Jmp(["ACTION_274_pause_38"]),
	SetSpriteSequence(index=9, looping_off=True, identifier="ACTION_274_set_sprite_sequence_74"),
	Jmp(["ACTION_274_pause_38"])
])
