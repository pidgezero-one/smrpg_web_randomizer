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
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	SetSpriteSequence(index=0, is_sequence=True, identifier="ACTION_206_set_sprite_sequence_2"),
	SetVarToConst(FACTORY_FALL_3, 0),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_10"]),
	Pause(7),
	Jmp(["ACTION_206_set_sprite_sequence_11"]),
	Pause(4, identifier="ACTION_206_pause_8"),
	Jmp(["ACTION_206_set_sprite_sequence_11"]),
	Pause(9, identifier="ACTION_206_pause_10"),
	SetSpriteSequence(index=3, is_sequence=True, identifier="ACTION_206_set_sprite_sequence_11"),
	SetVarToConst(FACTORY_FALL_3, 2),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_17"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_19"]),
	Pause(7),
	Jmp(["ACTION_206_set_sprite_sequence_20"]),
	Pause(4, identifier="ACTION_206_pause_17"),
	Jmp(["ACTION_206_set_sprite_sequence_20"]),
	Pause(9, identifier="ACTION_206_pause_19"),
	SetSpriteSequence(index=1, is_sequence=True, identifier="ACTION_206_set_sprite_sequence_20"),
	SetVarToConst(FACTORY_FALL_3, 1),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_26"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_28"]),
	Pause(7),
	Jmp(["ACTION_206_set_sprite_sequence_2"]),
	Pause(4, identifier="ACTION_206_pause_26"),
	Jmp(["ACTION_206_set_sprite_sequence_2"]),
	Pause(9, identifier="ACTION_206_pause_28"),
	Jmp(["ACTION_206_set_sprite_sequence_2"])
])
