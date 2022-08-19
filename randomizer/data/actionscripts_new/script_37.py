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
	SequenceLoopingOn(),
	Pause(40),
	ShiftSoutheastSteps(2),
	SetAllSpeeds(speed=FAST),
	JumpToHeight(96),
	ShiftSoutheastSteps(3),
	SetAllSpeeds(speed=NORMAL),
	FixedFCoordOn(),
	Walk1StepEast(),
	FixedFCoordOff(),
	Walk1StepNortheast(),
	SetAllSpeeds(speed=FAST),
	StartLoopNTimes(1),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	EndLoop(),
	SetBit(TEMP_7043_2),
	SetVRAMPriority(PRIORITY_3),
	SetAllSpeeds(speed=FAST),
	Walk1StepWest(),
	JumpToHeight(96),
	ShiftNorthwestSteps(3),
	SetAllSpeeds(speed=NORMAL),
	ShiftNorthwestSteps(4),
	PlaySound(sound=S065_THWOMP_STOMP, channel=4),
	SetSequenceSpeed(speed=SLOW),
	SetSpriteSequence(index=2, looping_off=True),
	Pause(40),
	SetSequenceSpeed(speed=NORMAL),
	ShiftWestSteps(3),
	ShiftNorthwestSteps(2),
	SetAllSpeeds(speed=FAST),
	JumpToHeight(96),
	ShiftNorthwestSteps(3),
	SetAllSpeeds(speed=NORMAL),
	ShiftNorthwestSteps(2),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	ShiftNorthwestSteps(2),
	SetPriority(3),
	Walk1StepNorthwest(),
	SetBit(TEMP_7043_3),
	Return()
])
