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
	VisibilityOff(identifier="ACTION_613_visibility_off_0"),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetPriority(3),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Pause(1),
	JmpIfVarNotEqualsConst(TEMP_70AE, 23, ["ACTION_613_visibility_off_0"]),
	VisibilityOn(),
	SetSequenceSpeed(speed=VERY_FAST),
	SequenceLoopingOn(),
	ShiftSoutheastPixels(18),
	ShiftZDownSteps(3),
	FaceMario(identifier="ACTION_613_face_mario_11"),
	Pause(1),
	Jmp(["ACTION_613_face_mario_11"])
])
