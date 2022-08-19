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
	SetSequenceSpeed(speed=FAST, identifier="ACTION_129_set_animation_speed_0"),
	ShiftSouthwestPixels(22),
	Walk1StepSouthwest(),
	Walk1StepSoutheast(),
	Walk1StepSoutheast(),
	ShiftSoutheastPixels(11),
	ShiftNortheastSteps(2),
	ShiftNortheastPixels(22),
	ShiftNorthwestPixels(11),
	ShiftNorthwestSteps(2),
	Walk1StepSouthwest(),
	FaceSoutheast(),
	Pause(1, identifier="ACTION_129_pause_12"),
	JmpIfBitSet(TEMP_7044_5, ["ACTION_129_set_animation_speed_0"]),
	Jmp(["ACTION_129_pause_12"])
])
