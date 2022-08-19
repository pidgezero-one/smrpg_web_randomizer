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
	VisibilityOff(),
	SetBit(TEMP_7043_7),
	SequenceLoopingOn(),
	Db(bytearray(b'\xfd\x12')),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True),
	Db(bytearray(b'\xc8\x98')),
	Db(bytearray(b'\x9a')),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	JumpToHeight(48),
	Walk1StepNorthwest(),
	SetVRAMPriority(NORMAL),
	Pause(1),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(45),
	ClearBit(TEMP_7043_7),
	Jmp(["ACTION_404_face_mario_3"])
])
