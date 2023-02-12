#A0293_MINES_FINAL_BOSS_ROOM_HENCHMAN_BASE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6], identifier="ACTION_293_object_memory_modify_bits_0"),
	FaceMario(),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(VERY_FAST),
	ShiftFDirectionSteps(2),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=COORD_F, pixel=True),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	Mem700CAndConst(0x0007),
	FaceEast7C(),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	ShiftFDirectionSteps(2),
	Return()
])
