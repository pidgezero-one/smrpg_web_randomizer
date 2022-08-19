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
	ShadowOff(),
	SetWalkingSpeed(speed=SLOW),
	ShiftSoutheastSteps(4),
	ShiftSoutheastPixels(8),
	ShadowOn(),
	JmpIfObjectInSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_in_level___2"]),
	WalkToXYCoords(x=9, y=29),
	ShiftEastPixels(10),
	Pause(32),
	SetSpriteSequence(index=5, is_sequence=True, mirror_sprite=True),
	Pause(112),
	SetBit(TEMP_7043_4),
	Pause(32),
	ResetProperties(),
	JmpIfObjectInSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_in_level___3"], identifier="ACTION_844_jmp_if_object_in_level___2"),
	WalkToXYCoords(x=8, y=25),
	Pause(32),
	SetSpriteSequence(index=5, is_sequence=True),
	Pause(112),
	SetBit(TEMP_7043_0),
	Pause(32),
	ResetProperties(),
	JmpIfObjectInSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_in_level___4"], identifier="ACTION_844_jmp_if_object_in_level___3"),
	WalkToXYCoords(x=6, y=29),
	Pause(32),
	SetSpriteSequence(index=5, is_sequence=True),
	Pause(112),
	SetBit(TEMP_7043_1),
	Pause(32),
	ResetProperties(),
	JmpIfObjectInSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_in_level___5"], identifier="ACTION_844_jmp_if_object_in_level___4"),
	WalkToXYCoords(x=8, y=34),
	Pause(32),
	SetSpriteSequence(index=5, is_sequence=True),
	Pause(112),
	SetBit(TEMP_7043_3),
	Pause(32),
	ResetProperties(),
	JmpIfObjectInSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_walk_to_xy_coords_13"], identifier="ACTION_844_jmp_if_object_in_level___5"),
	WalkToXYCoords(x=10, y=35),
	Pause(32),
	SetSpriteSequence(index=5, is_sequence=True),
	Pause(112),
	SetBit(TEMP_7043_5),
	Pause(32),
	ResetProperties(),
	WalkToXYCoords(x=7, y=28, identifier="ACTION_844_walk_to_xy_coords_13"),
	ShiftSouthwestSteps(4),
	ShiftSouthwestPixels(12),
	ShadowOff(),
	ShiftSouthwestSteps(14),
	VisibilityOff(),
	Return()
])
