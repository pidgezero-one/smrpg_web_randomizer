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
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6], identifier="ACTION_293_object_memory_modify_bits_0"),
	FaceMario(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftFDirectionSteps(2),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	Mem700CAndConst(0x0007),
	FaceEast7C(),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	ShiftFDirectionSteps(2),
	Return()
])
