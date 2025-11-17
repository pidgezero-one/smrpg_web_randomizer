#A0429_EMPTY

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
	A_SetPriority(3),
	A_JmpIfRandom1of2(["ACTION_429_transfer_xyzf_pixels_3"]),
	A_Pause(28),
	A_TransferXYZFPixels(x=2, y=255, z=0, direction=EAST, identifier="ACTION_429_transfer_xyzf_pixels_3"),
	A_Pause(8),
	A_TransferXYZFPixels(x=254, y=1, z=0, direction=EAST),
	A_Pause(8),
	A_TransferXYZFPixels(x=254, y=255, z=0, direction=EAST),
	A_Pause(8),
	A_TransferXYZFPixels(x=2, y=1, z=0, direction=EAST),
	A_Pause(8),
	A_Jmp(["ACTION_429_transfer_xyzf_pixels_3"])
])
