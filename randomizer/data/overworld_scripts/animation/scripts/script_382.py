#A0382_EMPTY

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
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(2),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(1),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZDownPixels(2),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZDownPixels(8),
	A_SetWalkingSpeed(NORMAL),
	A_ReturnQueue()
])
