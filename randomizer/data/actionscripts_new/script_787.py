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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 346, ["ACTION_787_set_animation_speed_10"]),
	SetWalkingSpeed(speed=VERY_FAST),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	SetPriority(3),
	FixedFCoordOn(),
	ShiftNorthwestSteps(2),
	FixedFCoordOff(),
	FaceNorthwest(),
	SetWalkingSpeed(speed=FASTEST, identifier="ACTION_787_set_animation_speed_10"),
	SequencePlaybackOff(),
	FixedFCoordOn(),
	ShiftNorthwestPixels(1, identifier="ACTION_787_shift_northwest_pixels_13"),
	ShiftSoutheastPixels(1),
	Jmp(["ACTION_787_shift_northwest_pixels_13"])
])
