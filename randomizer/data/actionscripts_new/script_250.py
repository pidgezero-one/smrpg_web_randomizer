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
	VisibilityOff(),
	FaceSoutheast(),
	TransferToXYZF(x=4, y=19, z=0, direction=EAST),
	TransferXYZFPixels(x=12, y=12, z=0, direction=EAST),
	ShadowOn(),
	VisibilityOn(),
	SetSpriteSequence(index=9, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(6),
	SetSpriteSequence(index=8, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(6),
	SetSpriteSequence(index=7, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(6),
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(6),
	ResetProperties(),
	SetSequenceSpeed(speed=FAST),
	SequencePlaybackOn(),
	ShiftSoutheastSteps(5),
	SequencePlaybackOff(),
	AddZCoord1Step(),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpSteps(2),
	SetWalkingSpeed(speed=VERY_FAST),
	SetBit(TEMP_7044_4),
	ShiftZUpSteps(2),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZUpSteps(4),
	ShadowOff(),
	SetWalkingSpeed(speed=NORMAL),
	TransferToXYZF(x=3, y=48, z=0, direction=EAST),
	SetBit(TEMP_7044_4),
	Return()
])
