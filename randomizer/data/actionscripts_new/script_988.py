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
	JmpIfBitSet(TEMP_7043_2, ["ACTION_988_set_animation_speed_3"]),
	TransferXYZFPixels(x=252, y=6, z=30, direction=NORTHEAST),
	SetSpriteSequence(index=3, is_sequence=True),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_988_set_animation_speed_3"),
	ShiftZDownPixels(1),
	Pause(8),
	ShiftZDownPixels(1),
	Pause(12),
	ShiftZUpPixels(1),
	Pause(8),
	ShiftZUpPixels(1),
	Pause(12),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_988_ret_14"]),
	Jmp(["ACTION_988_set_animation_speed_3"]),
	Return(identifier="ACTION_988_ret_14")
])
