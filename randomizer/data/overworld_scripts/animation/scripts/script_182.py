#A0182_EMPTY

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
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, identifier="ACTION_182_clear_solidity_bits_0"),
	A_SetWalkingSpeed(FAST),
	A_SequencePlaybackOff(),
	A_ShiftZUpPixels(12, identifier="ACTION_182_shift_z_up_pixels_3"),
	A_Pause(2),
	A_ShiftZDownPixels(12),
	A_Pause(2),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_182_pause_9"]),
	A_Jmp(["ACTION_182_shift_z_up_pixels_3"]),
	A_Pause(1, identifier="ACTION_182_pause_9"),
	A_JmpIfBitClear(TEMP_7044_5, ["ACTION_182_pause_9"]),
	A_Jmp(["ACTION_182_clear_solidity_bits_0"]),
	A_ReturnQueue()
])
