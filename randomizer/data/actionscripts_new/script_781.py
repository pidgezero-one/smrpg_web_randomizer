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
	JmpIfBitSet(SPINNING_FLOWER_1, ["ACTION_781_play_sound_12"]),
	SetBit(TEMP_7043_0),
	ClearSolidityBits(cant_pass_walls=True),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetVRAMPriority(PRIORITY_3),
	Db(bytearray(b'\xc8\x91')),
	SetWalkingSpeed(speed=SLOW),
	RunAwayShift(),
	SetWalkingSpeed(speed=NORMAL),
	SetVRAMPriority(NORMAL),
	ClearBit(TEMP_7043_0),
	Return(),
	PlaySound(sound=S034_SQUIRM_WRITHE, channel=4, identifier="ACTION_781_play_sound_12"),
	JumpToHeight(height=48, silent=True),
	RunAwayShift(),
	Return()
])
