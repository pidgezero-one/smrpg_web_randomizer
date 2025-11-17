#A0607_EMPTY

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(2),
	A_EndLoop(),
	A_SequenceLoopingOn(),
	A_SetAllSpeeds(NORMAL),
	A_JmpIfRandom1of2(["ACTION_607_pause_12"], identifier="ACTION_607_jmp_if_random_above_128_7"),
	A_TurnClockwise45DegreesNTimes(4),
	A_Walk1StepFDirection(),
	A_Pause(16),
	A_Jmp(["ACTION_607_jmp_if_random_above_128_7"]),
	A_Pause(1, identifier="ACTION_607_pause_12"),
	A_JmpIfRandom2of3(['ACTION_607_turn_clockwise_45_degrees_n_times_21', 'ACTION_607_set_700C_to_pressed_button_25']),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(16),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(6),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(16),
	A_TurnClockwise45DegreesNTimes(2),
	A_TurnClockwise45DegreesNTimes(4, identifier="ACTION_607_turn_clockwise_45_degrees_n_times_21"),
	A_Walk1StepFDirection(),
	A_Pause(16),
	A_Jmp(["ACTION_607_jmp_if_random_above_128_7"]),
	A_Set700CToPressedButton(identifier="ACTION_607_set_700C_to_pressed_button_25"),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 25),
	A_JmpIfComparisonResultIsLesser(["ACTION_607_start_loop_n_times_31"]),
	A_SetSpriteSequence(index=10, looping=False),
	A_Pause(30),
	A_Jmp(["ACTION_607_jmp_if_random_above_128_7"]),
	A_StartLoopNTimes(7, identifier="ACTION_607_start_loop_n_times_31"),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(5),
	A_EndLoop(),
	A_Jmp(["ACTION_607_jmp_if_random_above_128_7"])
])
