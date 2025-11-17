#A0832_EMPTY

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
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetPriority(3),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_SequencePlaybackOff(),
	A_ShiftToXYCoords(x=13, y=24),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Walk1StepSoutheast(),
	A_SequencePlaybackOn(),
	A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
	A_Pause(40),
	A_BPL262728(),
	A_ResetProperties(),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(12),
	A_WalkSouthwestSteps(16),
	A_ReturnQueue()
])
