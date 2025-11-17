#A0553_EMPTY

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
	A_WalkEastPixels(21),
	A_WalkSouthPixels(5),
	A_WalkSouthwestPixels(1),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_553_set_priority_15"]),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_553_set_priority_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_553_set_priority_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_553_set_priority_12"]),
	A_SetPriority(2),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetPriority(3, identifier="ACTION_553_set_priority_12"),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetPriority(2, identifier="ACTION_553_set_priority_15"),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_VisibilityOff(),
	A_ReturnQueue()
])
