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
	SetBit(TEMP_7043_0),
	SetBit(TEMP_7044_6),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(TEMP_7032, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 1280),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1281),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(SECONDARY_TEMP_7024, 1282),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1283),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_20"]),
	JmpIfBitSet(TEMP_7044_2, ["ACTION_783_play_sound_19"]),
	PlaySound(sound=S144_CLICK, channel=4),
	Jmp(["ACTION_783_set_sprite_sequence_20"]),
	PlaySound(sound=S143_METRONOME_UPBEAT_DING, channel=4, identifier="ACTION_783_play_sound_19"),
	SetSpriteSequence(index=2, is_sequence=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_20"),
	SetVarToConst(TEMP_7032, 5),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1282),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1281),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1280),
	Pause(6),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_31"]),
	PlaySound(sound=S144_CLICK, channel=4),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_31"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(TEMP_7032, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 256),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 257),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(SECONDARY_TEMP_7024, 258),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 259),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_49"]),
	JmpIfBitSet(TEMP_7044_2, ["ACTION_783_play_sound_48"]),
	PlaySound(sound=S143_METRONOME_UPBEAT_DING, channel=4),
	Jmp(["ACTION_783_set_sprite_sequence_49"]),
	PlaySound(sound=S144_CLICK, channel=4, identifier="ACTION_783_play_sound_48"),
	SetSpriteSequence(index=1, is_sequence=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_49"),
	SetVarToConst(TEMP_7032, 1),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 258),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 257),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 256),
	Pause(6),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_2"]),
	PlaySound(sound=S144_CLICK, channel=4),
	Jmp(["ACTION_783_set_sprite_sequence_2"]),
	ClearBit(TEMP_7044_6, identifier="ACTION_783_clear_bit_61"),
	ResetProperties(),
	Return()
])
