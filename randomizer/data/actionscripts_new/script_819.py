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
	SequenceLoopingOff(),
	FixedFCoordOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65516),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(9),
	EndLoop(),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_819_set_sprite_sequence_8"),
	Pause(16),
	SetSpriteSequence(index=2, is_sequence=True, mirror_sprite=True),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65515),
	AddConstToVar(PRIMARY_TEMP_700C, 25),
	SetMem704XAt700CBit(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	SetMem704XAt700CBit(),
	Pause(16),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65515),
	AddConstToVar(PRIMARY_TEMP_700C, 25),
	ClearMem704XAt700CBit(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	ClearMem704XAt700CBit(),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	Pause(16),
	SetSpriteSequence(index=1, is_sequence=True, mirror_sprite=True),
	Pause(16),
	Jmp(["ACTION_819_set_sprite_sequence_8"])
])
