#A0478_BANDITS_WAY_1ST_PLATFORMS_SWING
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
	A_SetPriority(2),
	A_VisibilityOff(),
	A_TransferToObjectXY(MEM_70A9),
	A_VisibilityOn(),
	A_ToggleSubroutineSlots(mask=0x03),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
	A_UnknownCommand(bytearray([0xFD, 0x25])),
	A_Pause(1, identifier="ACTION_478_pause_9"),
	A_Jmp(["ACTION_478_pause_9"])
])
