#A0630_EMPTY

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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	A_SetSequenceSpeed(FAST),
	A_WalkSouthPixels(8),
	A_FixedFCoordOff(),
	A_FaceNorthwest(),
	A_FixedFCoordOn(),
	A_WalkSouthPixels(8),
	A_SetSequenceSpeed(SLOW),
	A_Pause(30),
	A_FixedFCoordOff(),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(5),
	A_SetSequenceSpeed(SLOW),
	A_FaceNorthwest(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FASTEST),
	A_SetBit(TEMP_7044_0),
	A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	A_ClearBit(TEMP_7044_6),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_WalkNorthwestPixels(2, identifier="ACTION_630_shift_northwest_pixels_21"),
	A_WalkSoutheastPixels(2),
	A_Pause(16),
	A_WalkNorthwestPixels(2),
	A_WalkSoutheastPixels(2),
	A_Pause(60),
	A_Jmp(["ACTION_630_shift_northwest_pixels_21"])
])
