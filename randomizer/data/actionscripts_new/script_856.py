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
	SetWalkingSpeed(speed=VERY_FAST),
	Walk1StepSoutheast(identifier="ACTION_856_walk_1_step_southeast_1"),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(2),
	Walk1StepSoutheast(),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_856_face_northeast_8"]),
	Jmp(["ACTION_856_walk_1_step_southeast_1"]),
	FaceNortheast(identifier="ACTION_856_face_northeast_8"),
	SetWalkingSpeed(speed=NORMAL),
	SetBit(TEMP_7043_1),
	Return()
])
