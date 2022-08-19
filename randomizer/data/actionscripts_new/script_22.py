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
	JumpToHeight(height=80, silent=True, identifier="ACTION_22_jump_to_height_silent_0"),
	Pause(1, identifier="ACTION_22_pause_1"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_22_pause_1"]),
	Jmp(["ACTION_22_jump_to_height_silent_0"])
])
