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
	SequenceLoopingOn(identifier="ACTION_758_sequence_looping_on_0"),
	ShadowOff(),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastSteps(4),
	Pause(16),
	FaceNortheast(),
	Pause(16),
	ShiftNortheastSteps(4),
	Pause(16),
	FaceSoutheast(),
	Pause(16),
	ShiftSoutheastSteps(4),
	Pause(16),
	FaceNortheast(),
	Pause(16),
	ShiftNortheastSteps(4),
	Pause(16),
	FaceSouthwest(),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(16),
	ShiftSouthSteps(4),
	FaceSouthwest(),
	ResetProperties(),
	Pause(16),
	ShiftSouthwestSteps(4),
	Pause(16),
	FaceNorthwest(),
	Pause(16),
	ShiftNorthwestSteps(4),
	Pause(16),
	FaceSouthwest(),
	SetPriority(3),
	Pause(16),
	ShiftSouthwestSteps(4),
	Pause(16),
	FaceNorthwest(),
	Pause(16),
	ShiftNorthwestSteps(8),
	Pause(16),
	FaceNortheast(),
	Pause(16),
	ShiftNortheastSteps(4),
	SetPriority(2),
	Pause(16),
	FaceSoutheast(),
	Pause(16),
	Jmp(["ACTION_758_sequence_looping_on_0"])
])
