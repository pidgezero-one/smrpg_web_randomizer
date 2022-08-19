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
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_351_set_animation_speed_28"]),
	Db(bytearray(b'\xc8\x00')),
	TransferTo70167018(),
	SetPriority(3),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	VisibilityOn(identifier="ACTION_351_visibility_on_23"),
	Pause(30),
	VisibilityOff(),
	Pause(30),
	Jmp(["ACTION_351_visibility_on_23"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_351_set_animation_speed_28"),
	SetSequenceSpeed(speed=FAST),
	Walk1StepFDirection(),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_351_set_animation_speed_28"]),
	FaceMario(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	Walk1StepFDirection(),
	Jmp(["ACTION_351_set_animation_speed_28"])
])
