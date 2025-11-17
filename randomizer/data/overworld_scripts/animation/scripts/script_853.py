#A0853_EMPTY

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
	A_VisibilityOn(),
	A_SetSequenceSpeed(FASTER),
	A_SequenceLoopingOn(),
	A_ResetProperties(),
	A_WalkNortheastSteps(9),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_WalkNortheastPixels(8),
	A_Walk1StepSoutheast(),
	A_StartLoopNTimes(2),
	A_Walk1StepSoutheast(),
	A_WalkSoutheastPixels(6),
	A_JumpToHeight(0),
	A_WalkSoutheastPixels(10),
	A_EndLoop(),
	A_JumpToHeight(0),
	A_WalkSoutheastPixels(10),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestPixels(6),
	A_WalkSouthwestPixels(10),
	A_Walk1StepSouthwest(),
	A_WalkSouthwestSteps(4, identifier="ACTION_853_shift_southwest_steps_21"),
	A_WalkNorthwestSteps(7),
	A_WalkNortheastSteps(6),
	A_WalkSoutheastSteps(3),
	A_WalkSoutheastPixels(8),
	A_WalkSouthwestSteps(10),
	A_WalkNorthwestSteps(3),
	A_WalkNorthwestPixels(8),
	A_WalkNortheastSteps(8),
	A_WalkSoutheastSteps(7),
	A_Jmp(["ACTION_853_shift_southwest_steps_21"])
])
