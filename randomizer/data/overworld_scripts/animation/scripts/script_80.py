#A0080_EMPTY

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
	A_SetSequenceSpeed(FAST, identifier="ACTION_80_set_animation_speed_0"),
	A_StartLoopNTimes(8),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(12),
	A_VisibilityOff(),
	A_WalkSoutheastSteps(1),
	A_EndLoop(),
	A_StartLoopNTimes(8),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(12),
	A_VisibilityOff(),
	A_WalkNorthwestSteps(1),
	A_EndLoop(),
	A_Jmp(["ACTION_80_set_animation_speed_0"])
])
