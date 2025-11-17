#A0776_EMPTY

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
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkNorthwestSteps(18),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 16, identifier="ACTION_776_set_var_to_random_2"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 15),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(2),
	A_EndLoop(),
	A_JmpIfRandom2of3(['ACTION_776_set_animation_speed_14', 'ACTION_776_set_animation_speed_17']),
	A_Pause(31),
	A_JmpIfRandom2of3(['ACTION_776_set_animation_speed_14', 'ACTION_776_set_animation_speed_17']),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkSoutheastSteps(32),
	A_Pause(51),
	A_Jmp(["ACTION_776_set_var_to_random_2"]),
	A_SetWalkingSpeed(FASTEST, identifier="ACTION_776_set_animation_speed_14"),
	A_WalkSouthSteps(16),
	A_Pause(31),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_776_set_animation_speed_17"),
	A_WalkNorthwestSteps(32),
	A_Pause(51),
	A_Jmp(["ACTION_776_set_var_to_random_2"])
])
