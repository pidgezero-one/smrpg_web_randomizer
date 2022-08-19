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
	SetPriority(3, identifier="ACTION_311_set_priority_0"),
	SetWalkingSpeed(speed=SLOW),
	SetVarToConst(TEMP_70AE, 0),
	FaceMario(),
	Walk1StepFDirection(),
	ShadowOn(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 15, ["ACTION_311_set_700C_to_object_coord_12"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 111, ["ACTION_311_set_700C_to_object_coord_12"]),
	SetVarToConst(TEMP_70AE, 1),
	Jmp(["ACTION_311_face_mario_30"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_12"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 15, ["ACTION_311_set_700C_to_object_coord_18"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 113, ["ACTION_311_set_700C_to_object_coord_18"]),
	SetVarToConst(TEMP_70AE, 2),
	Jmp(["ACTION_311_face_mario_30"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_18"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_700C_to_object_coord_24"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 111, ["ACTION_311_set_700C_to_object_coord_24"]),
	SetVarToConst(TEMP_70AE, 3),
	Jmp(["ACTION_311_face_mario_30"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_24"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_priority_0"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 113, ["ACTION_311_set_priority_0"]),
	SetVarToConst(TEMP_70AE, 4),
	Jmp(["ACTION_311_face_mario_30"]),
	FaceMario(identifier="ACTION_311_face_mario_30"),
	Walk1StepFDirection(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_priority_0"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 112, ["ACTION_311_set_priority_0"]),
	Jmp(["ACTION_311_set_priority_0"])
])
