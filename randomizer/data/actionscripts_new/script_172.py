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
	FixedFCoordOn(),
	SetSpriteSequence(index=0, is_sequence=True),
	LoadMemory(TEMP_702E),
	Pause(1),
	JmpIfMarioInAir(["ACTION_172_ret_28"]),
	EndLoop(),
	StartLoopNTimes(11),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(2),
	ShiftZUpPixels(2),
	JmpIfMarioInAir(["ACTION_172_ret_28"]),
	EndLoop(),
	JumpToHeight(height=0, silent=True),
	FloatingOn(),
	Pause(1, identifier="ACTION_172_pause_14"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_172_pause_14"]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ShiftZUpSteps(9),
	StartLoopNTimes(4),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	EndLoop(),
	SetSolidityBits(cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Return(identifier="ACTION_172_ret_28")
])
