#A0018_EMPTY

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
	A_VisibilityOff(),
	A_ClearSolidityBits(cant_walk_through=True),
	A_SetSolidityBits(cant_jump_through=True),
	A_UnknownCommand(bytearray(b'\xc8\x80')),
	A_AddConstToVar(Z_COORD_2, 10),
	A_UnknownCommand(bytearray(b'\x9a')),
	A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_18_transfer_xyzf_pixels_14"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_18_transfer_xyzf_pixels_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_18_transfer_xyzf_pixels_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_18_transfer_xyzf_pixels_20"]),
	A_JmpIfRandom2of3(['ACTION_18_transfer_xyzf_pixels_18', 'ACTION_18_transfer_xyzf_pixels_20']),
	A_JmpIfRandom1of2(["ACTION_18_transfer_xyzf_pixels_16"]),
	A_Jmp(["ACTION_18_transfer_xyzf_pixels_14"]),
	A_TransferXYZFPixels(x=32, y=16, z=0, direction=EAST, identifier="ACTION_18_transfer_xyzf_pixels_14"),
	A_Jmp(["ACTION_18_db_21"]),
	A_TransferXYZFPixels(x=224, y=16, z=0, direction=EAST, identifier="ACTION_18_transfer_xyzf_pixels_16"),
	A_Jmp(["ACTION_18_db_21"]),
	A_TransferXYZFPixels(x=224, y=240, z=0, direction=EAST, identifier="ACTION_18_transfer_xyzf_pixels_18"),
	A_Jmp(["ACTION_18_db_21"]),
	A_TransferXYZFPixels(x=32, y=240, z=0, direction=EAST, identifier="ACTION_18_transfer_xyzf_pixels_20"),
	A_UnknownCommand(bytearray(b'\xc7\x07'), identifier="ACTION_18_db_21"),
	A_UnknownCommand(bytearray(b'\xc8\x87')),
	A_UnknownCommand(bytearray(b'\xfd\xca')),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 255, ["ACTION_18_ret_61"]),
	A_CompareVarToConst(X_COORD_1, 12544),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_18_ret_61"]),
	A_CompareVarToConst(X_COORD_1, 3584),
	A_JmpIfComparisonResultIsLesser(["ACTION_18_ret_61"]),
	A_CompareVarToConst(Y_COORD_1, 13056),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_18_ret_61"]),
	A_CompareVarToConst(Y_COORD_1, 8192),
	A_JmpIfComparisonResultIsLesser(["ACTION_18_ret_61"]),
	A_VisibilityOn(),
	A_FloatingOn(),
	A_Pause(1, identifier="ACTION_18_pause_35"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_18_pause_35"]),
	A_Pause(120),
	A_StartLoopNTimes(1),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(6),
	A_EndLoop(),
	A_StartLoopNTimes(3),
	A_VisibilityOff(),
	A_Pause(4),
	A_VisibilityOn(),
	A_Pause(4),
	A_EndLoop(),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_StartLoopNTimes(7),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_ClearBit(TEMP_7043_0),
	A_TransferToXYZF(x=21, y=117, z=0, direction=EAST),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_VisibilityOff(),
	A_ReturnQueue(identifier="ACTION_18_ret_61")
])
