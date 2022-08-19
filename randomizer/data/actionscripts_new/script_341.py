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
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_341_set_animation_speed_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_341_set_animation_speed_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_341_set_animation_speed_8"]),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_341_set_animation_speed_5"),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSoutheastSteps(5),
	SetAllSpeeds(speed=NORMAL, identifier="ACTION_341_set_animation_speed_8"),
	Walk1StepSoutheast(),
	Walk1StepSouthwest(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(3),
	SetAllSpeeds(speed=NORMAL),
	Walk1StepSoutheast(),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_341_set_animation_speed_16"),
	SetSequenceSpeed(speed=FAST),
	ShiftNortheastSteps(3),
	SetAllSpeeds(speed=NORMAL),
	ShiftNortheastSteps(2),
	ShiftNorthwestSteps(2),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_341_set_animation_speed_22"),
	SetSequenceSpeed(speed=FAST),
	ShiftNorthwestSteps(5),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepSouthwest(),
	Jmp(["ACTION_341_set_animation_speed_5"])
])
