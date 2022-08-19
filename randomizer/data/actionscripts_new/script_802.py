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
	FaceSouthwest(),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	JmpIfRandom1of2(["ACTION_802_fixed_f_coord_off_18"]),
	ShiftNortheastPixels(8),
	SequenceLoopingOff(),
	SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True),
	Pause(4),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthwestPixels(8),
	SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True),
	Pause(30),
	ResetProperties(),
	SetWalkingSpeed(speed=FAST),
	Pause(10),
	SetSpriteSequence(index=8, is_sequence=True),
	Pause(30),
	ResetProperties(),
	FixedFCoordOff(identifier="ACTION_802_fixed_f_coord_off_18"),
	Walk1StepEast(),
	Walk1StepNorth(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftNortheastSteps(4),
	ShiftNortheastPixels(4),
	ShiftNorthwestSteps(4),
	SequenceLoopingOff(),
	FaceSouthwest(),
	SetSolidityBits(cant_pass_walls=True),
	Return()
])
