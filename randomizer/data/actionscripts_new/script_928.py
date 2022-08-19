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
	JmpIfBitSet(MINECART_CLEARED, ["ACTION_928_visibility_off_17"], identifier="ACTION_928_jmp_if_bit_set_0"),
	SetWalkingSpeed(speed=SLOW),
	JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	ShiftNorthwestSteps(2),
	JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	ShiftNorthwestSteps(2),
	JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	ShiftSoutheastSteps(2),
	JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	ShiftSoutheastSteps(2),
	Jmp(["ACTION_928_jmp_if_bit_set_0"]),
	FaceNortheast(identifier="ACTION_928_face_northeast_11"),
	JumpToHeight(height=32, silent=True),
	Pause(12),
	JumpToHeight(height=32, silent=True),
	Pause(12),
	Return(),
	VisibilityOff(identifier="ACTION_928_visibility_off_17"),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return()
])
