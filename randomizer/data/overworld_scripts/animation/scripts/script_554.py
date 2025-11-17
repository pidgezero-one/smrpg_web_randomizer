#A0554_EMPTY

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
	A_WalkSouthwestPixels(7),
	A_WalkSoutheastPixels(3),
	A_WalkNorthPixels(7),
	A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 31, ["ACTION_554_set_priority_16"]),
	A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_554_set_priority_13"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_554_set_priority_13"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_554_set_priority_13"]),
	A_SetPriority(2),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetPriority(3, identifier="ACTION_554_set_priority_13"),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_SetPriority(2, identifier="ACTION_554_set_priority_16"),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_VisibilityOff(),
	A_ReturnQueue()
])
