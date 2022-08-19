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
	ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_103_clear_solidity_bits_0"),
	FloatingOff(),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=6),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZUpPixels(9),
	SetWalkingSpeed(speed=VERY_FAST, identifier="ACTION_103_set_animation_speed_5"),
	ShiftZUpPixels(5),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(3),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_103_set_animation_speed_9"),
	ShiftZUpPixels(2),
	SetWalkingSpeed(speed=SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_103_set_animation_speed_15"),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZDownPixels(2),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(3),
	SetWalkingSpeed(speed=VERY_FAST, identifier="ACTION_103_set_animation_speed_23"),
	ShiftZDownPixels(5),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZDownPixels(9),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_103_ret_29"]),
	Jmp(["ACTION_103_clear_solidity_bits_0"]),
	Return(identifier="ACTION_103_ret_29")
])
