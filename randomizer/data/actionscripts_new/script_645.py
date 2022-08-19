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
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_645_clear_bit_13"]),
	Pause(1, identifier="ACTION_645_pause_2"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_645_pause_2"]),
	Pause(1, identifier="ACTION_645_pause_4"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_645_pause_4"]),
	Pause(109),
	StartLoopNTimes(1),
	Pause(32),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(32),
	EndLoop(),
	Return(),
	ClearBit(MIDAS_RIVER_TUNNEL_1_BIT, identifier="ACTION_645_clear_bit_13"),
	Pause(168),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(64),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_2, ["ACTION_645_pause_22"]),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(35),
	SetBit(MIDAS_RIVER_TUNNEL_1_BIT),
	Return(),
	Pause(15, identifier="ACTION_645_pause_22"),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(36),
	SetSequenceSpeed(speed=SLOW),
	SetSpriteSequence(index=2, looping_off=True),
	Pause(50),
	FaceSoutheast(),
	Pause(40),
	SetSpriteSequence(index=4, looping_off=True, mirror_sprite=True),
	Return()
])
