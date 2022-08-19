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
	JmpIfBitSet(TEMP_7043_3, ["ACTION_635_transfer_to_xyzf_8"]),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_635_transfer_to_xyzf_11"]),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_635_transfer_to_xyzf_14"]),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_635_transfer_to_xyzf_20"]),
	JmpIfBitSet(TEMP_7044_1, ["ACTION_635_transfer_to_xyzf_17"]),
	TransferToXYZF(x=10, y=59, z=0, direction=SOUTHEAST),
	SetPriority(3),
	Jmp(["ACTION_635_visibility_on_22"]),
	TransferToXYZF(x=7, y=45, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_8"),
	SetPriority(3),
	Jmp(["ACTION_635_visibility_on_22"]),
	TransferToXYZF(x=13, y=34, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_11"),
	SetPriority(2),
	Jmp(["ACTION_635_visibility_on_22"]),
	TransferToXYZF(x=14, y=43, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_14"),
	SetPriority(3),
	Jmp(["ACTION_635_visibility_on_22"]),
	TransferToXYZF(x=17, y=59, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_17"),
	SetPriority(3),
	Jmp(["ACTION_635_visibility_on_22"]),
	TransferToXYZF(x=12, y=44, z=0, direction=SOUTHEAST, identifier="ACTION_635_transfer_to_xyzf_20"),
	SetPriority(3),
	VisibilityOn(identifier="ACTION_635_visibility_on_22"),
	ShadowOn(),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x00h\xff')),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastPixels(4),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastPixels(12),
	BPL262728(),
	ShadowOff(),
	Pause(1, identifier="ACTION_635_pause_32"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_635_pause_32"]),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	StartLoopNTimes(2),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(2),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(1),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(1),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(1),
	EndLoop(),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(1),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(1),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True),
	TransferToXYZF(x=21, y=79, z=0, direction=EAST),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_1),
	SetBit(TEMP_7044_5),
	Return()
])
