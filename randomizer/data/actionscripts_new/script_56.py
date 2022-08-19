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
	Set700CToCurrentLevel(identifier="ACTION_56_set_700C_to_current_level_0"),
	Pause(1),
	JmpIfBitClear(SEWER_WATER_LEVEL, ["ACTION_56_set_700C_to_current_level_0"]),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	SetSpriteSequence(index=1, looping_off=True, is_sequence=True),
	ClearSolidityBits(cant_walk_through=True, bit_7=True),
	Return()
])
