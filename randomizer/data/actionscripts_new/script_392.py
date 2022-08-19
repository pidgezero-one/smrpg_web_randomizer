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
	SetWalkingSpeed(speed=FAST, identifier="ACTION_392_set_animation_speed_0"),
	ShiftNorthPixels(5),
	ShiftSouthPixels(10),
	ShiftNorthPixels(5),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_392_ret_6"]),
	Jmp(["ACTION_392_set_animation_speed_0"]),
	Return(identifier="ACTION_392_ret_6")
])
