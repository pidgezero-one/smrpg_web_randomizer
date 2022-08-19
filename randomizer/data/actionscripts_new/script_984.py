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
	SetSequenceSpeed(speed=SLOW),
	SequenceLoopingOn(),
	Pause(1, identifier="ACTION_984_pause_2"),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_984_face_southwest_5"]),
	Jmp(["ACTION_984_pause_2"]),
	FaceSouthwest(identifier="ACTION_984_face_southwest_5"),
	Pause(30),
	FaceSoutheast(),
	Pause(30),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True),
	Pause(40),
	SetSequenceSpeed(speed=SLOW),
	SetSpriteSequence(index=0, is_sequence=True),
	Jmp(["ACTION_984_pause_2"])
])
