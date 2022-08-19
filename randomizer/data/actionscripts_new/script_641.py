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
	SetPriority(3),
	SetVRAMPriority(NORMAL),
	SequenceLoopingOn(),
	FixedFCoordOn(),
	Pause(8),
	StartLoopNTimes(5),
	SetAllSpeeds(speed=NORMAL),
	Walk1StepSouthwest(),
	SetSequenceSpeed(speed=FAST),
	ShiftSouthwestPixels(8),
	ShiftNortheastPixels(8),
	ShiftSouthwestPixels(8),
	ShiftNortheastPixels(8),
	SetSequenceSpeed(speed=NORMAL),
	Walk1StepNortheast(),
	EndLoop(),
	SetAllSpeeds(speed=FAST),
	Walk1StepSouthwest(),
	Pause(1, identifier="ACTION_641_pause_18"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_641_pause_18"]),
	SetAllSpeeds(speed=VERY_FAST),
	Walk1StepNortheast(),
	StartLoopNTimes(7),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	EndLoop(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	Pause(16),
	StartLoopNTimes(5),
	JumpToHeight(56),
	Walk1StepSoutheast(),
	JumpToHeight(56),
	Walk1StepNorthwest(),
	EndLoop(),
	ShiftEastSteps(2),
	Return()
])
