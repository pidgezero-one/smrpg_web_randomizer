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
	SetVarToConst(Y_COORD_1, 6),
	SetPriority(3),
	SetSequenceSpeed(speed=FAST),
	VisibilityOn(),
	SetSpriteSequence(index=10, is_sequence=True),
	Pause(10),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_570_set_sprite_sequence_6"),
	StartLoopNTimes(5),
	SetBit(TEMP_7044_3),
	Pause(20),
	ClearBit(TEMP_7044_3),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSoutheastPixels(10),
	SetWalkingSpeed(speed=FAST),
	ShiftSoutheastPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSoutheastPixels(2),
	Dec(Y_COORD_1),
	EndLoop(),
	SetSpriteSequence(index=1, is_sequence=True),
	StartLoopNTimes(5),
	SetBit(TEMP_7044_3),
	Pause(20),
	ClearBit(TEMP_7044_3),
	SetWalkingSpeed(speed=FASTEST),
	ShiftNorthwestPixels(10),
	SetWalkingSpeed(speed=FAST),
	ShiftNorthwestPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNorthwestPixels(2),
	Inc(Y_COORD_1),
	EndLoop(),
	Jmp(["ACTION_570_set_sprite_sequence_6"])
])
