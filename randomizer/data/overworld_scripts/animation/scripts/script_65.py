#A0065_EMPTY

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
	A_SetSequenceSpeed(FAST),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_WalkNortheastSteps(13),
	A_WalkNortheastPixels(8),
	A_SetBit(TEMP_7044_5),
	A_Pause(30),
	A_WalkNortheastSteps(1),
	A_WalkNortheastPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue()
])
