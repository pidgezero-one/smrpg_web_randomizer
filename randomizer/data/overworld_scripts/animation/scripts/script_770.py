#A0770_EMPTY

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
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetPriority(3),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_FixedFCoordOff(),
	A_ObjectMemorySetBit(arg_1=0x08, bits=[4]),
	A_FloatingOn(),
	A_SetAllSpeeds(VERY_FAST),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0001),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_770_transfer_to_xyzf_14"]),
	A_TransferToXYZF(x=15, y=37, z=0, direction=EAST),
	A_FaceNorthwest(),
	A_Jmp(["ACTION_770_visibility_on_16"]),
	A_TransferToXYZF(x=2, y=37, z=0, direction=EAST, identifier="ACTION_770_transfer_to_xyzf_14"),
	A_FaceNortheast(),
	A_VisibilityOn(identifier="ACTION_770_visibility_on_16"),
	A_WalkFDirectionSteps(10),
	A_Jmp(["ACTION_769_face_mario_6"])
])
