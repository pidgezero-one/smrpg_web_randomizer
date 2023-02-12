#A0364_BOOSTER_HILL_LEFTOVER_FLOWERS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(2),
	FixedFCoordOn(),
	SetWalkingSpeed(FAST),
	JmpIfRandom1of2(["ACTION_364_transfer_to_xyzf_6"]),
	TransferToXYZF(x=1, y=50, z=0, direction=EAST),
	Jmp(["ACTION_364_visibility_on_9"]),
	TransferToXYZF(x=2, y=48, z=0, direction=EAST, identifier="ACTION_364_transfer_to_xyzf_6"),
	Jmp(["ACTION_364_visibility_on_9"]),
	TransferToXYZF(x=3, y=46, z=0, direction=EAST),
	VisibilityOn(identifier="ACTION_364_visibility_on_9"),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Walk1StepSoutheast(identifier="ACTION_364_walk_1_step_southeast_12"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=COORD_X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_364_walk_1_step_southeast_12"]),
	Return()
])
