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
	ObjectMemorySetBit(arg_1=0x3C, bits=[6]),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	FloatingOff(),
	TransferToObjectXY(MARIO),
	JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	JmpIfRandom1of2(["ACTION_447_shift_xy_pixels_9"]),
	ShiftXYPixels(x=4, y=4),
	Jmp(["ACTION_447_sequence_looping_on_10"]),
	ShiftXYPixels(x=252, y=252, identifier="ACTION_447_shift_xy_pixels_9"),
	SequenceLoopingOn(identifier="ACTION_447_sequence_looping_on_10"),
	SetSpriteSequence(index=1, looping_off=True, is_sequence=True),
	StartLoopNTimes(23),
	JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	Pause(1),
	EndLoop(),
	VisibilityOff(identifier="ACTION_447_visibility_off_17"),
	Return()
])
