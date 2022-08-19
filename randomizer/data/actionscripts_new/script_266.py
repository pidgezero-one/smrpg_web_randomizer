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
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_266_set_animation_speed_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_266_pause_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_266_pause_7"]),
	Pause(3),
	Pause(3, identifier="ACTION_266_pause_7"),
	Pause(3, identifier="ACTION_266_pause_8"),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_266_set_animation_speed_9"),
	SequencePlaybackOff(),
	ShiftZDownSteps(4),
	FaceMario(),
	SequencePlaybackOn(),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(speed=FAST),
	SetSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(31),
	ShiftZUpPixels(2),
	ShiftFDirectionPixels(1),
	EndLoop(),
	Jmp(["ACTION_266_set_animation_speed_9"])
])
