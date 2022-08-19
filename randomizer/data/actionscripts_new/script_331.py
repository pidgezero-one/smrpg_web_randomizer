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
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_331_set_animation_speed_0"),
	SetSequenceSpeed(speed=FAST),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(2),
	Pause(30),
	ShiftSoutheastSteps(2),
	ShiftNortheastSteps(2),
	FaceSoutheast(),
	Pause(30),
	JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True),
	Pause(20),
	ResetProperties(),
	JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
	ShiftNorthwestSteps(2, identifier="ACTION_331_shift_northwest_steps_14"),
	Pause(60),
	ShiftSoutheastSteps(2),
	Pause(60),
	JmpIfRandom1of2(["ACTION_331_shift_northwest_steps_14"]),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True),
	Pause(20),
	ResetProperties(),
	Jmp(["ACTION_331_set_animation_speed_0"])
])
