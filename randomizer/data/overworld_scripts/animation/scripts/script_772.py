#A0772_EMPTY

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
	A_SetPriority(2),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SequenceLoopingOn(),
	A_FixedFCoordOn(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 12, identifier="ACTION_772_set_var_to_random_12"),
	A_Inc(PRIMARY_TEMP_700C),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(5),
	A_EndLoop(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_WalkNorthwestSteps(4),
	A_WalkSoutheastSteps(4),
	A_Jmp(["ACTION_772_set_var_to_random_12"])
])
