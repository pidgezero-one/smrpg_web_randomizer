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
	Pause(1, identifier="ACTION_644_pause_0"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_0"]),
	SetPriority(3),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Pause(1, identifier="ACTION_644_pause_5"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_5"]),
	Pause(26),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	Pause(1, identifier="ACTION_644_pause_10"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_644_pause_10"]),
	SetObjectMemoryBits(arg_1=0x0E),
	SetWalkingSpeed(speed=FAST),
	SetPriority(3),
	JumpToHeight(153),
	SetVRAMPriority(PRIORITY_3),
	BounceToXYWithHeight(x=17, y=58, height=0),
	SetWalkingSpeed(speed=VERY_FAST),
	AddZCoord1Step(),
	SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	Pause(1, identifier="ACTION_644_pause_21"),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_644_pause_21"]),
	SetWalkingSpeed(speed=FAST),
	JumpToHeight(48),
	ShiftNortheastSteps(3),
	Pause(1, identifier="ACTION_644_pause_26"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_26"]),
	JumpToHeight(80),
	Pause(17),
	FloatingOff(),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	Pause(1, identifier="ACTION_644_pause_32"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_32"]),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Pause(1, identifier="ACTION_644_pause_35"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_644_pause_35"]),
	Pause(13),
	SetObjectMemoryBits(arg_1=0x0E),
	JumpToHeight(16),
	Pause(14),
	FloatingOff(),
	Pause(10),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	Pause(1, identifier="ACTION_644_pause_44"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_644_pause_44"]),
	Pause(13),
	SetObjectMemoryBits(arg_1=0x0E),
	JumpToHeight(96),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_1, ["ACTION_644_shift_southwest_steps_63"]),
	ShiftSoutheastSteps(2),
	Pause(20),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	PlaySound(sound=S085_FLOWER, channel=4),
	StartLoopNTimes(7),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	SetBit(MIDAS_RIVER_TUNNEL_2_BIT_1),
	SetBit(TEMP_7043_4),
	Return(),
	ShiftSouthwestSteps(2, identifier="ACTION_644_shift_southwest_steps_63"),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepSouth(),
	Walk1StepSouthwest(),
	Walk1StepSouth(),
	VisibilityOff(),
	ClearBit(TEMP_7043_4),
	Return()
])
