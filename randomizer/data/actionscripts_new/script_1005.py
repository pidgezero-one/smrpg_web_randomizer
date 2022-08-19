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
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["ACTION_1005_ret_30"]),
	Pause(25),
	ResetProperties(),
	Pause(10),
	PlaySound(sound=S044_GHOST_FLOAT, channel=4),
	StartLoopNTimes(2),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	StartLoopNTimes(2),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(4),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(6),
	EndLoop(),
	VisibilityOff(),
	Return(identifier="ACTION_1005_ret_30")
])
