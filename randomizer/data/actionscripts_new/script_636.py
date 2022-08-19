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
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_636_pause_3"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_636_pause_3"]),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	Return()
])
