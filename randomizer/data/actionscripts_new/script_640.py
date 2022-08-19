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
	StartLoopNTimes(5),
	SetAllSpeeds(speed=NORMAL),
	Walk1StepNortheast(),
	SetSequenceSpeed(speed=FAST),
	JumpToHeight(56),
	Pause(16),
	JumpToHeight(56),
	Pause(16),
	SetSequenceSpeed(speed=NORMAL),
	Walk1StepSouthwest(),
	EndLoop(),
	SetAllSpeeds(speed=FAST),
	Walk1StepNortheast(),
	Pause(1, identifier="ACTION_640_pause_17"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_640_pause_17"]),
	SetAllSpeeds(speed=VERY_FAST),
	Walk1StepSouthwest(),
	StartLoopNTimes(7),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	EndLoop(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	StartLoopNTimes(5),
	JumpToHeight(56),
	Walk1StepNortheast(),
	JumpToHeight(56),
	Walk1StepSouthwest(),
	EndLoop(),
	ShiftNortheastSteps(5),
	Walk1StepEast(),
	Return()
])
