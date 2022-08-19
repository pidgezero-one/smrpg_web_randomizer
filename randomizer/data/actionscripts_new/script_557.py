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
	SetPriority(3),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x08\x80')),
	ShiftNorthwestSteps(5, identifier="ACTION_557_shift_northwest_steps_4"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northwest_steps_8"]),
	JmpIfRandom1of2(["ACTION_557_shift_northwest_steps_8"]),
	SetBit(TEMP_7043_0),
	ShiftNorthwestSteps(5, identifier="ACTION_557_shift_northwest_steps_8"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_12"]),
	JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_12"]),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(5, identifier="ACTION_557_shift_northeast_steps_12"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_16"]),
	JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_16"]),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(8, identifier="ACTION_557_shift_northeast_steps_16"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_20"]),
	JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_20"]),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(2, identifier="ACTION_557_shift_northeast_steps_20"),
	ShiftSoutheastSteps(5),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southeast_steps_25"]),
	JmpIfRandom1of2(["ACTION_557_shift_southeast_steps_25"]),
	SetBit(TEMP_7043_0),
	ShiftSoutheastSteps(5, identifier="ACTION_557_shift_southeast_steps_25"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_29"]),
	JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_29"]),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_29"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_33"]),
	JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_33"]),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_33"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_37"]),
	JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_37"]),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_37"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_557_jmp_41"]),
	JmpIfRandom1of2(["ACTION_557_jmp_41"]),
	SetBit(TEMP_7043_0),
	Jmp(["ACTION_557_shift_northwest_steps_4"], identifier="ACTION_557_jmp_41")
])
