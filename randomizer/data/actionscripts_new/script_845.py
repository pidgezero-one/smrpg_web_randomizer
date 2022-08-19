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
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True),
	VisibilityOn(),
	Pause(32),
	JmpIfRandom1of2(["ACTION_845_set_sprite_sequence_6"]),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Jmp(["ACTION_845_pause_7"]),
	Pause(1, identifier="ACTION_845_set_sprite_sequence_6"),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(48, identifier="ACTION_845_pause_7"),
	JmpIfRandom1of2(["ACTION_845_start_loop_n_times_22"], identifier="ACTION_845_jmp_if_random_above_128_8"),
	StartLoopNTimes(2),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(4),
	EndLoop(),
	Jmp(["ACTION_845_jmp_if_random_above_128_8"]),
	StartLoopNTimes(2, identifier="ACTION_845_start_loop_n_times_22"),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(2),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(4),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(8),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(2),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(4),
	EndLoop(),
	Jmp(["ACTION_845_jmp_if_random_above_128_8"])
])
