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
	Set700CToObjectCoord(object=MARIO, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_7038),
	JmpIf700CAnyBitsSet(bits=[0], destinations=["ACTION_671_jmp_if_bit_set_4"]),
	SetBit(YOSTER_ISLE_LIBERATED_1),
	JmpIfBitSet(TEMP_7049_2, ["ACTION_671_jmp_if_bit_set_6"], identifier="ACTION_671_jmp_if_bit_set_4"),
	SetSequenceSpeed(speed=VERY_FAST),
	JmpIfBitSet(YOSTER_ISLE_LIBERATED_1, ["ACTION_671_set_700C_to_70A0_short_mem_11"], identifier="ACTION_671_jmp_if_bit_set_6"),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 1, ["ACTION_671_set_sprite_sequence_19"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 3, ["ACTION_671_set_sprite_sequence_21"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 5, ["ACTION_671_set_sprite_sequence_23"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 7, ["ACTION_671_set_sprite_sequence_25"]),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C, identifier="ACTION_671_set_700C_to_70A0_short_mem_11"),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AB),
	Db(bytearray(b'\xfd$\x00\x13')),
	Mem700CAndConst(0x00C0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_671_set_sprite_sequence_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["ACTION_671_set_sprite_sequence_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["ACTION_671_set_sprite_sequence_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["ACTION_671_set_sprite_sequence_25"]),
	SetSpriteSequence(index=8, is_sequence=True, mirror_sprite=True, identifier="ACTION_671_set_sprite_sequence_19"),
	Jmp(["ACTION_671_set_bit_26"]),
	SetSpriteSequence(index=8, is_sequence=True, identifier="ACTION_671_set_sprite_sequence_21"),
	Jmp(["ACTION_671_set_bit_26"]),
	SetSpriteSequence(index=9, is_sequence=True, identifier="ACTION_671_set_sprite_sequence_23"),
	Jmp(["ACTION_671_set_bit_26"]),
	SetSpriteSequence(index=9, is_sequence=True, mirror_sprite=True, identifier="ACTION_671_set_sprite_sequence_25"),
	SetBit(TEMP_7043_6, identifier="ACTION_671_set_bit_26"),
	JmpIfBitSet(UNKNOWN_704A_3, ["ACTION_671_pause_31"]),
	Pause(4),
	StopSound(),
	PlaySound(sound=S056_SHAKE_HEAD, channel=4),
	Pause(32, identifier="ACTION_671_pause_31"),
	StopSound(),
	SequenceLoopingOff(),
	SetSequenceSpeed(speed=NORMAL),
	ResetProperties(),
	CopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	ClearBit(YOSTER_ISLE_LIBERATED_1),
	ClearBit(TEMP_7049_2),
	ClearBit(UNKNOWN_704A_3),
	ClearBit(TEMP_7043_6),
	Return()
])
