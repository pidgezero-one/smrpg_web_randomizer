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
	JmpIfBitClear(MINES_BACK_OPENED, ["ACTION_615_visibility_off_3"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["ACTION_615_visibility_off_3"]),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	VisibilityOff(identifier="ACTION_615_visibility_off_3"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
