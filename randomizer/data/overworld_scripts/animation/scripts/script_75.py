#A0075_EMPTY

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
	A_Walk1StepNorthwest(),
	A_Pause(70),
	A_SetSequenceSpeed(FAST),
	A_SequenceLoopingOn(),
	A_Walk1StepSoutheast(),
	A_SequenceLoopingOff(),
	A_Pause(32),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(),
	A_Walk1StepNorthwest(),
	A_SequenceLoopingOff(),
	A_Pause(120),
	A_SequenceLoopingOn(),
	A_Walk1StepSoutheast(),
	A_SequenceLoopingOff(),
	A_Pause(240),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_FixedFCoordOff(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkSoutheastSteps(1),
	A_WalkSouthwestSteps(3),
	A_FaceSouthwest(),
	A_Pause(240),
	A_FaceNortheast(),
	A_Pause(360),
	A_FaceSoutheast(),
	A_Pause(60),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkNortheastSteps(3),
	A_FaceSoutheast(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_FixedFCoordOn(),
	A_Walk1StepNorthwest(),
	A_SequenceLoopingOff(),
	A_FixedFCoordOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ReturnQueue()
])
