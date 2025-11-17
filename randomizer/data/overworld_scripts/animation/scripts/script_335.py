#A0335_EMPTY

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
	A_Pause(32),
	A_VisibilityOff(),
	A_TransferToXYZF(x=15, y=87, z=0, direction=EAST),
	A_TransferXYZFPixels(x=240, y=0, z=20, direction=EAST),
	A_VisibilityOn(),
	A_TurnRandomDirection(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_FloatingOn(),
	A_JumpToHeight(height=128, silent=True),
	A_SetWalkingSpeed(FAST),
	A_WalkFDirectionSteps(5),
	A_ReturnQueue()
])
