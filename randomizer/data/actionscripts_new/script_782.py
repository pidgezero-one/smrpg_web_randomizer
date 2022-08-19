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
	SetSpriteSequence(index=0, is_sequence=True, identifier="ACTION_782_set_sprite_sequence_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(TEMP_7032, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 1792),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1793),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(SECONDARY_TEMP_7024, 1794),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1795),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_782_clear_bit_55"]),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_782_set_sprite_sequence_17"]),
	PlaySound(sound=S143_METRONOME_UPBEAT_DING, channel=4),
	SetSpriteSequence(index=2, is_sequence=True, identifier="ACTION_782_set_sprite_sequence_17"),
	SetVarToConst(TEMP_7032, 7),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1794),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1793),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 1792),
	Pause(6),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_782_set_sprite_sequence_28"]),
	PlaySound(sound=S144_CLICK, channel=4),
	SetSpriteSequence(index=0, is_sequence=True, identifier="ACTION_782_set_sprite_sequence_28"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(TEMP_7032, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 768),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 769),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	SetVarToConst(SECONDARY_TEMP_7024, 770),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 771),
	Pause(6),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_782_clear_bit_55"]),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_782_set_sprite_sequence_43"]),
	PlaySound(sound=S144_CLICK, channel=4),
	SetSpriteSequence(index=1, is_sequence=True, identifier="ACTION_782_set_sprite_sequence_43"),
	SetVarToConst(TEMP_7032, 3),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 770),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 769),
	Pause(6),
	SetVarToConst(SECONDARY_TEMP_7024, 768),
	Pause(6),
	JmpIfBitClear(TEMP_7044_4, ["ACTION_782_set_sprite_sequence_2"]),
	PlaySound(sound=S144_CLICK, channel=4),
	Jmp(["ACTION_782_set_sprite_sequence_2"]),
	ClearBit(TEMP_7044_6, identifier="ACTION_782_clear_bit_55"),
	ResetProperties(),
	Return()
])
