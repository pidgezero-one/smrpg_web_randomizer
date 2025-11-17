#A0764_EMPTY

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
	A_StartLoopNTimes(1),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNortheastSteps(2),
	A_JumpToHeight(height=108, silent=True),
	A_WalkSouthwestSteps(2),
	A_EndLoop(),
	A_FaceNorthwest(),
	A_Pause(4),
	A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(32),
	A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\x00\xff\x10\xff')),
	A_UnknownCommand(bytearray(b'%\x00\n\x80\xff')),
	A_Pause(38),
	A_BPL262728(),
	A_SetBit(TEMP_7043_0),
	A_ShiftZDownPixels(8),
	A_FaceNorthwest(),
	A_ResetProperties(),
	A_ReturnQueue()
])
