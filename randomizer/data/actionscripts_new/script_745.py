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
	SequenceLoopingOn(identifier="ACTION_745_sequence_looping_on_0"),
	ShadowOff(),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNortheastSteps(3),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSoutheastSteps(4),
	ShiftSoutheastPixels(8),
	Pause(24),
	FaceSouthwest(),
	Pause(24),
	ShiftSouthwestSteps(8),
	Pause(24),
	FaceNorthwest(),
	Pause(24),
	ShiftNorthwestSteps(8),
	Pause(24),
	FaceNortheast(),
	Pause(24),
	ShiftNortheastSteps(3),
	ShiftNortheastPixels(4),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSoutheastSteps(3),
	ShiftSoutheastPixels(8),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	WalkToXYCoords(x=10, y=107),
	Jmp(["ACTION_745_sequence_looping_on_0"])
])
