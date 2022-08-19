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
	FloatingOn(identifier="ACTION_99_floating_on_0"),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_99_pause_3"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_99_pause_3"]),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_99_ret_9"]),
	Jmp(["ACTION_99_floating_on_0"]),
	Return(identifier="ACTION_99_ret_9")
])
