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
	SetPriority(3, identifier="ACTION_60_set_priority_0"),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_60_pause_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_60_pause_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_60_pause_9"]),
	Pause(3),
	Pause(3, identifier="ACTION_60_pause_7"),
	Pause(3, identifier="ACTION_60_pause_8"),
	Pause(3, identifier="ACTION_60_pause_9"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	TurnRandomDirection(),
	SetWalkingSpeed(speed=FAST),
	StartLoopNTimes(2),
	Set700CToObjectCoord(object=MARIO, coord=Z, pixel=True),
	AddConstToVar(PRIMARY_TEMP_700C, 224),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Z, pixel=True),
	DecVarFrom700C(TEMP_7028),
	JmpIfLoadedMemoryIs0(["ACTION_60_jmp_24"]),
	JmpIfLoadedMemoryIsBelow0(["ACTION_60_shift_z_down_pixels_25"]),
	JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_60_shift_z_up_pixels_27"]),
	Jmp(["ACTION_60_walk_1_step_f_direction_28"], identifier="ACTION_60_jmp_24"),
	ShiftZDownPixels(8, identifier="ACTION_60_shift_z_down_pixels_25"),
	Jmp(["ACTION_60_walk_1_step_f_direction_28"]),
	ShiftZUpPixels(8, identifier="ACTION_60_shift_z_up_pixels_27"),
	Walk1StepFDirection(identifier="ACTION_60_walk_1_step_f_direction_28"),
	EndLoop(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ResetProperties(),
	PlaySound(sound=S044_GHOST_FLOAT, channel=4),
	StartLoopNTimes(3),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	FaceMario(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	Mem700CAndConst(0x0006),
	Inc(PRIMARY_TEMP_700C),
	FaceEast7C(),
	SequenceLoopingOn(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_60_set_sprite_sequence_50"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_60_set_sprite_sequence_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_60_set_sprite_sequence_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_60_set_sprite_sequence_50"]),
	SetSpriteSequence(index=3, looping_off=True, is_sequence=True, mirror_sprite=True, identifier="ACTION_60_set_sprite_sequence_50"),
	Jmp(["ACTION_60_set_animation_speed_53"]),
	SetSpriteSequence(index=3, looping_off=True, is_sequence=True, identifier="ACTION_60_set_sprite_sequence_52"),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_60_set_animation_speed_53"),
	ShiftFDirectionSteps(3),
	SequenceLoopingOff(),
	PlaySound(sound=S000_SILENCE, channel=6),
	StartLoopNTimes(3),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	VisibilityOff(),
	Jmp(["ACTION_60_set_priority_0"])
])
