#A0222_EMPTY

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
	A_TransferXYZFPixels(x=0, y=0, z=2, direction=EAST),
	A_SetSequenceSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepSoutheast(identifier="ACTION_222_walk_1_step_southeast_7"),
	A_Pause(90),
	A_FixedFCoordOff(),
	A_Walk1StepNortheast(),
	A_JmpIfRandom1of2(["ACTION_222_walk_1_step_southeast_21"]),
	A_WalkNortheastSteps(3, identifier="ACTION_222_shift_northeast_steps_12"),
	A_Walk1StepNorthwest(),
	A_Pause(120),
	A_FixedFCoordOn(),
	A_Walk1StepSoutheast(),
	A_Pause(90),
	A_FixedFCoordOff(),
	A_WalkSouthwestSteps(3),
	A_JmpIfRandom1of2(["ACTION_222_walk_1_step_southwest_28"]),
	A_Walk1StepSoutheast(identifier="ACTION_222_walk_1_step_southeast_21"),
	A_WalkSoutheastPixels(8),
	A_FaceNortheast(),
	A_Pause(120),
	A_Walk1StepNorthwest(),
	A_WalkNorthwestPixels(8),
	A_JmpIfRandom1of2(["ACTION_222_shift_northeast_steps_12"]),
	A_Walk1StepSouthwest(identifier="ACTION_222_walk_1_step_southwest_28"),
	A_Walk1StepNorthwest(),
	A_Pause(120),
	A_FixedFCoordOn(),
	A_Jmp(["ACTION_222_walk_1_step_southeast_7"])
])
