#A0836_EMPTY

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
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestSteps(2),
	A_Walk1StepSouthwest(),
	A_WalkSoutheastSteps(4),
	A_WalkSouthwestSteps(3),
	A_Walk1StepNorthwest(),
	A_WalkNortheastSteps(4),
	A_WalkSoutheastSteps(2),
	A_WalkSouthwestSteps(16),
	A_ReturnQueue()
])
