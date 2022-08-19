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
	ShiftSoutheastSteps(4, identifier="ACTION_688_shift_southeast_steps_4"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southeast_steps_8"]),
	JmpIfRandom2of3(['ACTION_688_shift_southeast_steps_8', 'ACTION_688_shift_southeast_steps_8']),
	SetBit(TEMP_7043_0),
	ShiftSoutheastSteps(5, identifier="ACTION_688_shift_southeast_steps_8"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_12"]),
	JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_12', 'ACTION_688_shift_southwest_steps_12']),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(4, identifier="ACTION_688_shift_southwest_steps_12"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_16"]),
	JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_16', 'ACTION_688_shift_southwest_steps_16']),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(3, identifier="ACTION_688_shift_southwest_steps_16"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_20"]),
	JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_20', 'ACTION_688_shift_northwest_steps_20']),
	SetBit(TEMP_7043_0),
	ShiftNorthwestSteps(2, identifier="ACTION_688_shift_northwest_steps_20"),
	ShiftSouthwestSteps(3),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_25"]),
	JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_25', 'ACTION_688_shift_southwest_steps_25']),
	SetBit(TEMP_7043_0),
	ShiftSouthwestSteps(2, identifier="ACTION_688_shift_southwest_steps_25"),
	ShiftNortheastSteps(3),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_30"]),
	JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_30', 'ACTION_688_shift_northeast_steps_30']),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(2, identifier="ACTION_688_shift_northeast_steps_30"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southeast_steps_34"]),
	JmpIfRandom2of3(['ACTION_688_shift_southeast_steps_34', 'ACTION_688_shift_southeast_steps_34']),
	SetBit(TEMP_7043_0),
	ShiftSoutheastSteps(2, identifier="ACTION_688_shift_southeast_steps_34"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_38"]),
	JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_38', 'ACTION_688_shift_northeast_steps_38']),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(4, identifier="ACTION_688_shift_northeast_steps_38"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_42"]),
	JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_42', 'ACTION_688_shift_northeast_steps_42']),
	SetBit(TEMP_7043_0),
	ShiftNortheastSteps(3, identifier="ACTION_688_shift_northeast_steps_42"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_46"]),
	JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_46', 'ACTION_688_shift_northwest_steps_46']),
	SetBit(TEMP_7043_0),
	ShiftNorthwestSteps(5, identifier="ACTION_688_shift_northwest_steps_46"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_50"]),
	JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_50', 'ACTION_688_shift_northwest_steps_50']),
	SetBit(TEMP_7043_0),
	ShiftNorthwestSteps(4, identifier="ACTION_688_shift_northwest_steps_50"),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_688_jmp_54"]),
	JmpIfRandom2of3(['ACTION_688_jmp_54', 'ACTION_688_jmp_54']),
	SetBit(TEMP_7043_0),
	Jmp(["ACTION_688_shift_southeast_steps_4"], identifier="ACTION_688_jmp_54")
])
