#A0248_ENDING_CUTSCENE_EFFECT
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
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x7F, 0xFF, 0x00, 0xEE, 0xFF, 0x80, 0xFE, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xE4, 0x00, 0x5C, 0xFF, 0x00, 0xEE, 0xFF, 0x80, 0xFE, 0x80])),
	A_SetWalkingSpeed(VERY_SLOW),
	A_AddZCoord1Step(),
	A_Pause(392),
	A_KillAllSubroutineSlots(),
	A_ReturnQueue()
])
