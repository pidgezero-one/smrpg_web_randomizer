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
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	SetAllSpeeds(speed=NORMAL, identifier="ACTION_476_set_animation_speed_6"),
	StartLoopNTimes(2),
	TurnClockwise45DegreesNTimes(2),
	Pause(5),
	EndLoop(),
	Pause(16),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	Walk1StepFDirection(),
	Pause(16),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	Jmp(["ACTION_476_set_animation_speed_6"]),
	SetAllSpeeds(speed=FAST, identifier="ACTION_476_set_animation_speed_17"),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(2),
	EndLoop(),
	Jmp(["ACTION_476_set_animation_speed_6"])
])
