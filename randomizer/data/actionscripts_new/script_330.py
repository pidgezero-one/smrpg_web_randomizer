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
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_330_set_animation_speed_0"),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(3),
	FaceSouthwest(),
	SetSpriteSequence(index=3, is_sequence=True),
	Pause(20),
	ResetProperties(),
	ShiftNorthwestSteps(3),
	Pause(60),
	JmpIfRandom1of2(["ACTION_330_set_animation_speed_0"]),
	ShiftSouthwestSteps(2, identifier="ACTION_330_shift_southwest_steps_10"),
	FaceNorthwest(),
	Pause(30),
	ShiftNortheastSteps(2),
	FaceNorthwest(),
	Pause(60),
	JmpIfRandom1of2(["ACTION_330_shift_southwest_steps_10"]),
	Jmp(["ACTION_330_set_animation_speed_0"])
])
