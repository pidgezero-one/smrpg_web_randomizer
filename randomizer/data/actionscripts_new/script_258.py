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
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_258_set_animation_speed_0"),
	SetSequenceSpeed(speed=FAST),
	TurnRandomDirection(),
	JumpToHeight(height=80, silent=True),
	Pause(1, identifier="ACTION_258_pause_4"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_258_pause_4"]),
	Walk1StepNortheast(),
	TurnRandomDirection(),
	JumpToHeight(height=80, silent=True),
	Pause(1, identifier="ACTION_258_pause_9"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_258_pause_9"]),
	Walk1StepSouthwest(),
	Jmp(["ACTION_258_set_animation_speed_0"])
])
