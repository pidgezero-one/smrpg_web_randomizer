#A0859_ABYSS_BEFORE_1ST_BOSS_SCREW_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(1, identifier="ACTION_859_pause_0"),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetWalkingSpeed(NORMAL),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_859_pause_0"]),
	JmpIfBitClear(TEMP_7044_6, ["ACTION_859_pause_0"]),
	Set700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_859_jmp_if_var_equals_const_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_859_jmp_if_var_equals_const_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_859_jmp_if_var_equals_const_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_859_jmp_if_var_equals_const_19"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 16, ["ACTION_859_pause_0"]),
	Inc(FACTORY_FALL_3),
	SetSpriteSequence(index=1, looping=False),
	ShiftNortheastPixels(5),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7044_6),
	Jmp(["ACTION_859_pause_0"]),
	JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["ACTION_859_pause_0"], identifier="ACTION_859_jmp_if_var_equals_const_19"),
	Dec(FACTORY_FALL_3),
	SetSpriteSequence(index=2, looping=False),
	ShiftSouthwestPixels(5),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7044_6),
	Jmp(["ACTION_859_pause_0"])
])
