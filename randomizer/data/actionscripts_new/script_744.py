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
	SequenceLoopingOn(identifier="ACTION_744_sequence_looping_on_0"),
	ShadowOff(),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestSteps(4),
	ShiftSouthwestPixels(7),
	Pause(32),
	FaceNorthwest(),
	Pause(24),
	ShiftNorthwestSteps(3),
	ShiftNorthwestPixels(7),
	Pause(16),
	FaceNortheast(),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthwestPixels(3),
	SetSequenceSpeed(speed=SLOW),
	Pause(384),
	ShiftNortheastPixels(3),
	FixedFCoordOff(),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepSouthwest(),
	ShiftSoutheastSteps(8),
	ShiftSoutheastPixels(5),
	SetSequenceSpeed(speed=SLOW),
	Pause(32),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(4),
	ShiftNortheastPixels(7),
	Pause(32),
	SequenceLoopingOff(),
	Pause(64),
	SetWalkingSpeed(speed=VERY_SLOW),
	WalkToXYCoords(x=12, y=71),
	Jmp(["ACTION_744_sequence_looping_on_0"])
])
