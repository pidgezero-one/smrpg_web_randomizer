#A0499_MUSHROOM_DERBY_UNKNOWN
# pyright: reportWildcardImportFromLibrary=false

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
	A_ToggleSubroutineSlots(mask=0x03),
	A_SetSubroutineXTargets(slot_26_x=0x00E0, slot_27_x=0xFF90),
	A_Pause(4),
	A_SetSubroutineXTargets(slot_26_x=0x0040, slot_27_x=0xFFE0),
	A_Pause(2)
])
