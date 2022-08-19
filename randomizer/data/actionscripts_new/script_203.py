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
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_203_set_animation_speed_28"]),
	VisibilityOff(),
	ShiftEastPixels(6),
	ShiftZUpPixels(5),
	ResetProperties(),
	FaceSouthwest(),
	Pause(60),
	VisibilityOn(),
	SetSpriteSequence(index=0, looping_off=True, is_sequence=True),
	Pause(16),
	PlaySound(sound=S118_BECKONING_TENTACLE, channel=4),
	Pause(56),
	SetSpriteSequence(index=1, is_sequence=True),
	Pause(60),
	SetSpriteSequence(index=2, looping_off=True, is_sequence=True),
	Pause(24),
	VisibilityOff(),
	Return(),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_203_set_animation_speed_28"),
	SetSequenceSpeed(speed=FAST),
	Walk1StepFDirection(),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_203_set_animation_speed_28"]),
	FaceMario(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	Walk1StepFDirection(),
	Jmp(["ACTION_203_set_animation_speed_28"])
])
