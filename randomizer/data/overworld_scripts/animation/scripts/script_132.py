#A0132_HENCHMAN_BONKING_HOUSE
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
	A_SetPriority(3, identifier="ACTION_132_set_priority_0"),
	A_UnknownCommand(bytearray([0x20, 0x04])),
	A_UnknownCommand(bytearray([0x25, 0x00, 0x07, 0xA0, 0xFF])),
	A_SetWalkingSpeed(SLOW),
	A_WalkNorthwestPixels(16),
	A_BPL262728(),
	A_FaceSoutheast(),
	A_UnknownCommand(bytearray([0x20, 0x04])),
	A_UnknownCommand(bytearray([0x25, 0x00, 0x04, 0xA0, 0xFF])),
	A_WalkSoutheastPixels(16),
	A_BPL262728(),
	A_Jmp(["ACTION_132_set_priority_0"])
])
