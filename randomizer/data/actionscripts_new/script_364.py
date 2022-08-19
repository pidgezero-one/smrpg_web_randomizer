#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SetPriority(2),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=FAST),
	JmpIfRandom1of2(["ACTION_364_transfer_to_xyzf_6"]),
	TransferToXYZF(x=1, y=50, z=0, direction=EAST),
	Jmp(["ACTION_364_visibility_on_9"]),
	TransferToXYZF(x=2, y=48, z=0, direction=EAST, identifier="ACTION_364_transfer_to_xyzf_6"),
	Jmp(["ACTION_364_visibility_on_9"]),
	TransferToXYZF(x=3, y=46, z=0, direction=EAST),
	VisibilityOn(identifier="ACTION_364_visibility_on_9"),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Walk1StepSoutheast(identifier="ACTION_364_walk_1_step_southeast_12"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_364_walk_1_step_southeast_12"]),
	Return()
])
