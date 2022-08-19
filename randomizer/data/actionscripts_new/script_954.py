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
	SetWalkingSpeed(speed=SLOW),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	WalkToXYCoords(x=16, y=94),
	ShiftToXYCoords(x=8, y=35),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	ShiftSoutheastSteps(5),
	Jmp(["ACTION_953_set_animation_speed_0"])
])
