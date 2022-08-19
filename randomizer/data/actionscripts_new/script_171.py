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
	SequenceLoopingOn(),
	JmpIfBitSet(MINECART_INITIATE_FREEPLAY, ["ACTION_171_set_animation_speed_11"]),
	SetWalkingSpeed(speed=FAST),
	SetSpriteSequence(index=1, is_sequence=True),
	JumpToHeight(80),
	FaceEast7C(),
	ShiftFDirectionPixels(48),
	VisibilityOff(),
	Return(),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_171_set_animation_speed_11"),
	SetSpriteSequence(index=1, is_sequence=True),
	JumpToHeight(96),
	ShiftSoutheastPixels(17),
	VisibilityOff(),
	Return()
])
