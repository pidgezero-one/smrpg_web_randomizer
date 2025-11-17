#A0097_EMPTY

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
	A_Pause(120),
	A_TransferToXYZF(x=8, y=106, z=0, direction=EAST),
	A_SetWalkingSpeed(SLOW),
	A_FixedFCoordOff(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ClearSolidityBits(bit_0=True),
	A_FloatingOn(),
	A_WalkNortheastSteps(5),
	A_WalkNorthwestSteps(5),
	A_WalkNortheastSteps(2),
	A_WalkSoutheastSteps(4),
	A_FaceNortheast(),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ReturnQueue()
])
