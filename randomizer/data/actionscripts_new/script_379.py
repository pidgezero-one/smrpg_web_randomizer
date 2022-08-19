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
	FaceSouthwest(identifier="ACTION_379_face_southwest_0"),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_379_pause_2"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_379_pause_2"]),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_379_face_southeast_6"]),
	Jmp(["ACTION_379_face_southwest_0"]),
	FaceSoutheast(identifier="ACTION_379_face_southeast_6"),
	Pause(1, identifier="ACTION_379_pause_7"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_379_face_southwest_0"]),
	Jmp(["ACTION_379_pause_7"])
])
