#A0501_MUSHROOM_DERBY_UNKNOWN
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
	A_KillAllSubroutineSlots(),
	A_SetSequenceSpeed(VERY_FAST),
	A_ToggleSubroutineSlots(mask=0x03),
	A_SetSubroutineXTargets(slot_26_x=0x0140, slot_27_x=0xFF60),
	A_Pause(14),
	A_SetBit(TEMP_7043_2),
	A_Jmp(["ACTION_500_db_0"])
])
