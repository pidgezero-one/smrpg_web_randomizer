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
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True, identifier="ACTION_509_clear_solidity_bits_0"),
	SetPriority(3),
	VisibilityOn(),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(5),
	SetWalkingSpeed(speed=FASTEST),
	SetSpriteSequence(index=1, is_sequence=True),
	PlaySound(sound=S084_SMOKED, channel=6),
	AddZCoord1Step(),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	AddZCoord1Step(),
	SetWalkingSpeed(speed=VERY_FAST),
	AddZCoord1Step(),
	SetWalkingSpeed(speed=FASTER),
	ShiftZUpPixels(8),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(4),
	StartLoopNTimes(3),
	SetSpriteSequence(index=2, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=3, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=4, is_sequence=True),
	Pause(4),
	EndLoop(),
	SetSpriteSequence(index=4, is_sequence=True),
	ShiftZDownPixels(4),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(4),
	SetWalkingSpeed(speed=FASTER),
	ShiftZDownPixels(8),
	SetWalkingSpeed(speed=VERY_FAST),
	DecZCoord1Step(),
	SetWalkingSpeed(speed=FASTEST),
	SetSpriteSequence(index=2, is_sequence=True),
	DecZCoord1Step(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	DecZCoord1Step(),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(5),
	VisibilityOff(),
	Pause(90),
	Jmp(["ACTION_509_clear_solidity_bits_0"])
])
