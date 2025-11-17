#A0072_EMPTY

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
	A_FixedFCoordOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_JumpToHeight(height=48, silent=True),
	A_SetWalkingSpeed(FAST),
	A_Walk1StepNortheast(),
	A_Pause(70),
	A_FloatingOff(),
	A_SetSequenceSpeed(FAST),
	A_SequenceLoopingOn(),
	A_Walk1StepSouthwest(),
	A_SequenceLoopingOff(),
	A_Pause(32),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(),
	A_Walk1StepNortheast(),
	A_SequenceLoopingOff(),
	A_Pause(120),
	A_SequenceLoopingOn(),
	A_Walk1StepSouthwest(),
	A_SequenceLoopingOff(),
	A_Pause(260),
	A_FixedFCoordOff(),
	A_TurnRandomDirection(),
	A_Pause(20),
	A_TurnRandomDirection(),
	A_Pause(20),
	A_TurnRandomDirection(),
	A_Pause(20),
	A_TurnRandomDirection(),
	A_Pause(20),
	A_TurnRandomDirection(),
	A_Pause(20),
	A_FaceSouthwest(),
	A_ReturnQueue()
])
