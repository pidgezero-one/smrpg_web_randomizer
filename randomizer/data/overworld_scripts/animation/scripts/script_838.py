#A0838_EMPTY

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
	A_SequenceLoopingOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_WalkNortheastPixels(8),
	A_SetAllSpeeds(FAST),
	A_Walk1StepNortheast(),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNortheastSteps(2),
	A_WalkNortheastPixels(8),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestPixels(8),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNorthwestSteps(3),
	A_WalkNorthwestPixels(8),
	A_Walk1StepNortheast(),
	A_WalkNortheastPixels(8),
	A_SetBit(TEMP_7043_0),
	A_Walk1StepNorthwest(),
	A_WalkNorthwestPixels(8),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNorthwestSteps(3),
	A_WalkNorthwestSteps(2),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(48),
	A_ResetProperties(),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepSoutheast(),
	A_WalkSoutheastPixels(8),
	A_Pause(4),
	A_FaceSouthwest(),
	A_Pause(4),
	A_WalkNorthPixels(4),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNorthwestSteps(2),
	A_WalkNorthwestPixels(8),
	A_Pause(8),
	A_JumpToHeight(height=108, silent=True),
	A_WalkNorthwestSteps(3),
	A_Pause(4),
	A_FaceWest(),
	A_Pause(4),
	A_FaceSouthwest(),
	A_Pause(4),
	A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetBit(TEMP_7043_1),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$0\xfe\x00\x02')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(20),
	A_BPL262728(),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
