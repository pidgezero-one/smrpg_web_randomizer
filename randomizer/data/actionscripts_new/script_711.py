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
	FixedFCoordOn(),
	Dec(TEMP_70AE),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	SetAllSpeeds(speed=VERY_FAST),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_711_db_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_711_db_16"]),
	Db(bytearray(b' \x00')),
	Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_8"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_8"]),
	TransferToXYZF(x=13, y=67, z=0, direction=EAST),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_15"]),
	JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_15"),
	Db(bytearray(b' \x00'), identifier="ACTION_711_db_16"),
	Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_17"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_17"]),
	TransferToXYZF(x=12, y=69, z=0, direction=EAST),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_24"]),
	JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_24"),
	Db(bytearray(b' \x00'), identifier="ACTION_711_db_25"),
	Walk1StepSoutheast(identifier="ACTION_711_walk_1_step_southeast_26"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_711_walk_1_step_southeast_26"]),
	TransferToXYZF(x=11, y=71, z=0, direction=EAST),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_711_jmp_34"]),
	TransferToXYZF(x=12, y=70, z=0, direction=EAST),
	JmpToSubroutine(["ACTION_712_set_700C_to_pressed_button_0"]),
	Jmp(["ACTION_707_set_priority_0"], identifier="ACTION_711_jmp_34")
])
