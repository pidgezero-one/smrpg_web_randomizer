#A0409_EMPTY

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
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=128, tiles=3, destinations=["ACTION_409_clear_solidity_bits_17"], identifier="ACTION_409_jmp_if_object_within_range_2"),
	A_JmpIfRandom1of2(["ACTION_409_jmp_if_random_above_128_10"]),
	A_FaceMario(),
	A_Pause(8),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 2),
	A_Inc(PRIMARY_TEMP_700C),
	A_ShiftZUp20Steps(),
	A_Jmp(["ACTION_409_jmp_if_object_within_range_2"]),
	A_JmpIfRandom1of2(["ACTION_409_set_var_to_random_13"], identifier="ACTION_409_jmp_if_random_above_128_10"),
	A_TurnRandomDirection(),
	A_Pause(8),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 2, identifier="ACTION_409_set_var_to_random_13"),
	A_Inc(PRIMARY_TEMP_700C),
	A_ShiftZUp20Steps(),
	A_Jmp(["ACTION_409_jmp_if_object_within_range_2"]),
	A_ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_409_clear_solidity_bits_17"),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x07')),
	A_BPL2627(),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b'0\x00\x02')),
	A_UnknownCommand(bytearray(b')\x00')),
	A_Pause(192),
	A_BPL262728(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_Jmp(["ACTION_409_jmp_if_object_within_range_2"])
])
