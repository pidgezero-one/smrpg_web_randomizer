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
	VisibilityOn(),
	Pause(117),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["ACTION_45_reset_properties_13"]),
	JumpToHeight(108),
	ShiftSouthwestSteps(2),
	SetBit(MIDAS_RIVER_TUNNEL_4_PRIZE),
	StartLoopNTimes(4),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	Return(),
	ResetProperties(identifier="ACTION_45_reset_properties_13"),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FASTER),
	Walk1StepEast(),
	Walk1StepWest(),
	Jmp(["ACTION_45_reset_properties_13"])
])
