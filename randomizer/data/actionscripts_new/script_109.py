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
	SetPriority(3),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZUpPixels(20),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZUpPixels(10),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(2),
	SetWalkingSpeed(speed=SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZDownPixels(2),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(4),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZDownPixels(10),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZDownPixels(20),
	Pause(2),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(speed=FASTEST, identifier="ACTION_109_set_animation_speed_28"),
	ShiftZUpPixels(20),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZUpPixels(10),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(2),
	SetWalkingSpeed(speed=SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZDownPixels(2),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(4),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZDownPixels(10),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZDownPixels(20),
	Pause(2),
	Jmp(["ACTION_109_set_animation_speed_28"])
])
