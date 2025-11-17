#A0383_EMPTY

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
	A_SetWalkingSpeed(VERY_FAST),
	A_ResetProperties(),
	A_WalkNortheastPixels(8),
	A_WalkNortheastSteps(3),
	A_FloatingOff(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkNorthwestSteps(3),
	A_WalkNortheastSteps(1),
	A_Jmp(["ACTION_113_jmp_if_bit_set_0"])
])
