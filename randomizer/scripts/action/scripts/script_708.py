#A0708_BOOSTER_HILL_BARREL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(2),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetAllSpeeds(FASTER),
	TransferToXYZF(x=1, y=50, z=0, direction=EAST),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	SetVarToRandom(PRIMARY_TEMP_700C, 30),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	JmpIfBitSet(TEMP_7044_4, ["ACTION_708_shift_southwest_pixels_14"]),
	PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
	ShiftSouthwestPixels(8, identifier="ACTION_708_shift_southwest_pixels_14"),
	JmpIfObjectWithinRange(object=NPC_3, usually=0, tiles=3, destinations=["ACTION_708_set_bit_19"], identifier="ACTION_708_db_15"),
	JumpToHeight(24),
	Walk1StepSoutheast(),
	Jmp(["ACTION_708_db_15"]),
	SetBit(TEMP_7043_0, identifier="ACTION_708_set_bit_19"),
	JumpToHeight(24, identifier="ACTION_708_jump_to_height_20"),
	Walk1StepSoutheast(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=COORD_X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_708_jump_to_height_20"]),
	Return()
])
