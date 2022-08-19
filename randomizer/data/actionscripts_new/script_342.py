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
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_342_set_animation_speed_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_342_set_animation_speed_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_342_set_animation_speed_8"]),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_342_set_animation_speed_5"),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(7),
	SetAllSpeeds(speed=NORMAL, identifier="ACTION_342_set_animation_speed_8"),
	ShiftSouthwestSteps(2),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(2),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_342_set_animation_speed_12"),
	SetSequenceSpeed(speed=FAST),
	ShiftNortheastSteps(7),
	SetAllSpeeds(speed=NORMAL, identifier="ACTION_342_set_animation_speed_15"),
	ShiftNortheastSteps(3),
	Walk1StepNorthwest(),
	ShiftSouthwestSteps(3),
	Jmp(["ACTION_342_set_animation_speed_5"])
])
