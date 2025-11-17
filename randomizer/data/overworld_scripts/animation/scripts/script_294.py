#A0294_EMPTY

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
	A_ShadowOn(),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x18\x00o\x00\x01\xf2\xff\x00\xff\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xe0\x00\x7f\x00\x01\xf2\xff\x00\xff\x80")),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpSteps(6),
	A_Pause(240),
	A_SetVarToConst(PRIMARY_TEMP_700C, 255),
	A_UnknownCommand(bytearray(b'5\x00\x04')),
	A_UnknownCommand(bytearray(b'5\x01\x04')),
	A_Pause(420),
	A_BPL262728(),
	A_ReturnQueue()
])
