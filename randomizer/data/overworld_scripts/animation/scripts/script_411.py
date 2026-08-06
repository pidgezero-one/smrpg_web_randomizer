#A0411_FOREST_MAZE_AREA_BEE
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
	A_SetPriority(3),
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_ToggleSubroutineSlots(mask=0x07),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x18, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_Pause(1, identifier="ACTION_411_pause_7"),
	A_Jmp(["ACTION_411_pause_7"])
])
