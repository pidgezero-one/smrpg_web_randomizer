#A0510_EMPTY

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
	A_JmpIfBitSet(NIMBUS_HOUSE_ITEM_RETRIEVED, ["ACTION_510_set_animation_speed_42"]),
	A_ResetProperties(),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_510_start_loop_n_times_14"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_510_turn_clockwise_45_degrees_n_times_11"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_510_start_loop_n_times_38"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_510_start_loop_n_times_35"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_510_start_loop_n_times_31"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_510_start_loop_n_times_27"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_510_start_loop_n_times_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_510_start_loop_n_times_19"]),
	A_TurnClockwise45DegreesNTimes(1, identifier="ACTION_510_turn_clockwise_45_degrees_n_times_11"),
	A_Pause(2),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(1, identifier="ACTION_510_start_loop_n_times_14"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_EndLoop(),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(2, identifier="ACTION_510_start_loop_n_times_19"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(3, identifier="ACTION_510_start_loop_n_times_23"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(4, identifier="ACTION_510_start_loop_n_times_27"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(5, identifier="ACTION_510_start_loop_n_times_31"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_Jmp(["ACTION_510_start_loop_n_times_38"]),
	A_StartLoopNTimes(6, identifier="ACTION_510_start_loop_n_times_35"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_StartLoopNTimes(6, identifier="ACTION_510_start_loop_n_times_38"),
	A_TurnClockwise45DegreesNTimes(1),
	A_Pause(2),
	A_EndLoop(),
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_510_set_animation_speed_42"),
	A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
	A_Pause(20),
	A_SetSequenceSpeed(SLOW),
	A_Pause(40),
	A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(20),
	A_ResetProperties(),
	A_ClearBit(NIMBUS_HOUSE_ITEM_RETRIEVED),
	A_ReturnQueue()
])
