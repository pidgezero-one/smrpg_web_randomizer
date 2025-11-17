#A0024_EMPTY

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
	A_WalkSouthwestSteps(2),
	A_FaceNorthwest(identifier="ACTION_24_face_northwest_1"),
	A_Pause(60),
	A_WalkNortheastSteps(3),
	A_JmpIfRandom1of2(["ACTION_24_walk_1_step_northeast_8"]),
	A_FaceNorthwest(identifier="ACTION_24_face_northwest_5"),
	A_Pause(30),
	A_JmpIfRandom1of2(["ACTION_24_shift_southwest_steps_12"]),
	A_Walk1StepNortheast(identifier="ACTION_24_walk_1_step_northeast_8"),
	A_Pause(90),
	A_Walk1StepSouthwest(),
	A_JmpIfRandom1of2(["ACTION_24_face_northwest_5"]),
	A_WalkSouthwestSteps(3, identifier="ACTION_24_shift_southwest_steps_12"),
	A_Jmp(["ACTION_24_face_northwest_1"])
])
