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
	Pause(25, identifier="ACTION_442_pause_0"),
	FaceMario(),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=5, destinations=["ACTION_442_set_animation_speed_4"]),
	Jmp(["ACTION_442_pause_0"]),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_442_set_animation_speed_4"),
	SequencePlaybackOn(),
	SetSolidityBits(cant_pass_walls=True),
	ShiftFDirectionSteps(2),
	FaceMario(),
	ShiftFDirectionSteps(2),
	FaceMario(),
	ShiftFDirectionSteps(2),
	SequencePlaybackOff(),
	Jmp(["ACTION_442_pause_0"])
])
