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
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	SetSpriteSequence(index=1, is_sequence=True),
	Pause(1, identifier="ACTION_336_pause_5"),
	JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_336_pause_5"]),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=1, destinations=["ACTION_336_pause_5"]),
	JmpIfObjectWithinRange(object=NPC_0, usually=208, tiles=0, destinations=["ACTION_336_pause_5"]),
	Dec(TEMP_70AE),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	SetSpriteSequence(index=0, is_sequence=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetVRAMPriority(NORMAL),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Return()
])
