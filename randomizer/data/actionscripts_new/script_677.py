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
	JmpIfRandom2of3(['ACTION_677_pause_2', 'ACTION_677_pause_3'], identifier="ACTION_677_jmp_if_random_above_66_0"),
	Pause(30),
	Pause(30, identifier="ACTION_677_pause_2"),
	Pause(30, identifier="ACTION_677_pause_3"),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_677_pause_5"),
	JmpIfBitSet(TEMP_7044_7, ["ACTION_677_pause_9"]),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_5"]),
	Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
	Pause(1, identifier="ACTION_677_pause_9"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_677_pause_9"]),
	FaceNortheast(),
	Return()
])
