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
	SetWalkingSpeed(speed=FASTEST),
	Walk1StepNorthwest(),
	ShiftNorthwestPixels(4),
	FaceNortheast(),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_970_start_loop_n_times_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_970_start_loop_n_times_23"]),
	StartLoopNTimes(9),
	SetSpriteSequence(index=3, looping_off=True, mirror_sprite=True),
	Pause(34),
	EndLoop(),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(80),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, mirror_sprite=True),
	Return(),
	StartLoopNTimes(10, identifier="ACTION_970_start_loop_n_times_15"),
	SetSpriteSequence(index=3, looping_off=True, mirror_sprite=True),
	Pause(34),
	EndLoop(),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(64),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, mirror_sprite=True),
	Return(),
	StartLoopNTimes(11, identifier="ACTION_970_start_loop_n_times_23"),
	SetSpriteSequence(index=3, looping_off=True, mirror_sprite=True),
	Pause(34),
	EndLoop(),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(48),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, mirror_sprite=True),
	Return()
])
