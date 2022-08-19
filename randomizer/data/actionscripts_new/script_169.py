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
	Pause(2),
	EndLoop(),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_169_set_animation_speed_6"),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=3, is_sequence=True),
	Walk1StepSouthwest(),
	Pause(9),
	ResetProperties(),
	Pause(9),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	StartLoopNTimes(2),
	TurnClockwise45DegreesNTimes(6),
	Walk1StepFDirection(),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	EndLoop(),
	Pause(15),
	FaceSoutheast(),
	Pause(15),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True),
	Walk1StepSoutheast(),
	Pause(9),
	ResetProperties(),
	Pause(9),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	StartLoopNTimes(2),
	TurnClockwise45DegreesNTimes(2),
	Walk1StepFDirection(),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	EndLoop(),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=6, destinations=["ACTION_169_set_animation_speed_39"]),
	Jmp(["ACTION_169_set_animation_speed_6"]),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_169_set_animation_speed_39"),
	SetSequenceSpeed(speed=VERY_FAST),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(2),
	EndLoop(),
	Jmp(["ACTION_169_set_animation_speed_6"])
])
