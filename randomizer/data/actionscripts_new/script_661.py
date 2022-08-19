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
	SetSpriteSequence(index=0, is_sequence=True),
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_661_set_animation_speed_1"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=2, destinations=["ACTION_661_set_animation_speed_5"]),
	Pause(1),
	Jmp(["ACTION_661_set_animation_speed_1"]),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_661_set_animation_speed_5"),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_661_pause_7"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_661_pause_7"]),
	Jmp(["ACTION_661_set_animation_speed_1"])
])
