#A0552_EMPTY

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
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES, identifier="ACTION_552_set_vram_priority_0"),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\xb0\x00\xe0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
	A_Pause(2),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\xb0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
	A_Pause(22),
	A_BPL262728(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
