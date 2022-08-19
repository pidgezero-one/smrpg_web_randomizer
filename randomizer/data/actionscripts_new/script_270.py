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
	SetMovementsBits(bit_0=True, cant_walk_under=True),
	SetPriority(3),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_270_set_animation_speed_2"),
	SequencePlaybackOff(),
	ShiftZDownSteps(5),
	FaceMario(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032),
	SequencePlaybackOn(),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(speed=FAST),
	SetSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(39),
	ShiftZUpPixels(2),
	ShiftFDirectionPixels(1),
	EndLoop(),
	Jmp(["ACTION_270_set_animation_speed_2"])
])
