#A0809_MARIO_BLOWN_BY_FAN
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_809_db_6"]),
	A_ToggleSubroutineSlots(mask=0x03),
	A_SetSubroutineXTargets(slot_26_x=0xFE00, slot_27_x=0x0100),
	A_Pause(1, identifier="ACTION_809_pause_4"),
	A_Jmp(["ACTION_809_pause_4"]),
	A_ToggleSubroutineSlots(mask=0x03, identifier="ACTION_809_db_6"),
	A_SetSubroutineXTargets(slot_26_x=0x0200, slot_27_x=0x0100),
	A_Jmp(["ACTION_809_pause_4"])
])
