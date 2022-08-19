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
	Pause(59),
	VisibilityOn(),
	TransferToXYZF(x=11, y=49, z=0, direction=SOUTHEAST),
	ShiftXYPixels(x=8, y=253),
	SetBit(TEMP_7044_3, identifier="ACTION_638_set_bit_4"),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x00r\xff')),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepNortheast(),
	ShiftNortheastPixels(12),
	BPL262728(),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	StartLoopNTimes(2),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(2),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(2),
	EndLoop(),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2),
	VisibilityOff(),
	TransferToXYZF(x=22, y=78, z=0, direction=EAST),
	ClearBit(TEMP_7044_3),
	Return()
])
