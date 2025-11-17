#A0624_EMPTY

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
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	A_SetAllSpeeds(VERY_FAST),
	A_WalkNortheastPixels(12),
	A_VisibilityOn(),
	A_WalkNortheastPixels(4),
	A_WalkNortheastSteps(7),
	A_WalkNortheastPixels(4),
	A_Walk1StepNorthwest(),
	A_SetSequenceSpeed(SLOW),
	A_SetBit(TEMP_7044_5),
	A_ClearBit(TEMP_7043_7),
	A_ReturnQueue()
])
