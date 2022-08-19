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
	JmpIfBitSet(TEMP_7043_6, ["ACTION_102_jmp_if_random_above_128_6"]),
	JmpIfRandom2of3(['ACTION_103_clear_solidity_bits_0', 'ACTION_102_transfer_xyzf_pixels_4']),
	TransferXYZFPixels(x=0, y=0, z=9, direction=EAST),
	Jmp(["ACTION_103_set_animation_speed_5"]),
	TransferXYZFPixels(x=0, y=0, z=17, direction=EAST, identifier="ACTION_102_transfer_xyzf_pixels_4"),
	Jmp(["ACTION_103_set_animation_speed_9"]),
	JmpIfRandom1of2(["ACTION_101_pause_9"], identifier="ACTION_102_jmp_if_random_above_128_6"),
	Pause(30),
	Jmp(["ACTION_103_clear_solidity_bits_0"]),
	Pause(10),
	Jmp(["ACTION_103_clear_solidity_bits_0"])
])
