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
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	SetVarToConst(FACTORY_FALL_3, 0, identifier="ACTION_186_set_2"),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(4),
	SetVarToConst(FACTORY_FALL_3, 2),
	SetSpriteSequence(index=3, is_sequence=True),
	Pause(4),
	SetVarToConst(FACTORY_FALL_3, 1),
	SetSpriteSequence(index=1, is_sequence=True),
	Pause(4),
	Jmp(["ACTION_186_set_2"])
])
