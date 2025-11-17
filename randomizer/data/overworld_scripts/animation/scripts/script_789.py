#A0789_EMPTY

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
	A_FixedFCoordOn(),
	A_FloatingOff(),
	A_SetWalkingSpeed(VERY_FAST),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_Walk1StepSoutheast(),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_Pause(30),
	A_SequenceLoopingOff(),
	A_SequencePlaybackOff(),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(2),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZDownPixels(4),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZDownPixels(9),
	A_FixedFCoordOn(),
	A_WalkSoutheastPixels(1, identifier="ACTION_789_shift_southeast_pixels_18"),
	A_WalkNorthwestPixels(1),
	A_Jmp(["ACTION_789_shift_southeast_pixels_18"])
])
