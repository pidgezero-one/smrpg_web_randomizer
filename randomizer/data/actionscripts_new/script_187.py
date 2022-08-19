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
	Pause(1, identifier="ACTION_187_pause_0"),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=NORMAL),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_187_pause_0"]),
	JmpIfBitClear(TEMP_7044_6, ["ACTION_187_pause_0"]),
	Set700CToObjectCoord(object=MARIO, coord=F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_187_jmp_if_var_equals_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_187_jmp_if_var_equals_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_187_jmp_if_var_equals_const_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_187_jmp_if_var_equals_const_18"]),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 24, ["ACTION_187_pause_0"]),
	Inc(FACTORY_FALL_2),
	SetSpriteSequence(index=1, looping_off=True),
	ShiftNortheastPixels(5),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_6),
	Jmp(["ACTION_187_pause_0"]),
	JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["ACTION_187_pause_0"], identifier="ACTION_187_jmp_if_var_equals_const_18"),
	Dec(FACTORY_FALL_2),
	SetSpriteSequence(index=2, looping_off=True),
	ShiftSouthwestPixels(5),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_6),
	Jmp(["ACTION_187_pause_0"])
])
