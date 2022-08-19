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
	SetWalkingSpeed(speed=FASTEST, identifier="ACTION_959_set_animation_speed_0"),
	ShadowOff(),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	ShiftWestPixels(4),
	SetWalkingSpeed(speed=SLOW),
	SetBit(TEMP_7044_1),
	ShiftNorthSteps(2),
	ShiftNorthPixels(8),
	JmpIfBitSet(TEMP_7044_0, ["ACTION_959_shift_z_up_steps_11"], identifier="ACTION_959_jmp_if_bit_set_8"),
	Pause(1),
	Jmp(["ACTION_959_jmp_if_bit_set_8"]),
	ShiftZUpSteps(3, identifier="ACTION_959_shift_z_up_steps_11"),
	WalkToXYCoords(x=3, y=88),
	ShadowOn(),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastPixels(8),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownSteps(3),
	Pause(12),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	WalkToXYCoords(x=10, y=103),
	ShiftToXYCoords(x=1, y=77),
	JmpIfBitSet(TEMP_7044_2, ["ACTION_959_ret_25"]),
	Jmp(["ACTION_959_set_animation_speed_0"]),
	Return(identifier="ACTION_959_ret_25")
])
