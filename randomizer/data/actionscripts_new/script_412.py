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
	SetPriority(3),
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	Db(bytearray(b' \x07')),
	JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_7"]),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	Jmp(["ACTION_412_jmp_if_random_above_128_8"]),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80'), identifier="ACTION_412_embedded_animation_routine_7"),
	JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_11"], identifier="ACTION_412_jmp_if_random_above_128_8"),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80")),
	Jmp(["ACTION_412_jmp_if_random_above_128_12"]),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80"), identifier="ACTION_412_embedded_animation_routine_11"),
	JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_15"], identifier="ACTION_412_jmp_if_random_above_128_12"),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\x00\x00\x00\x04\x80')),
	Jmp(["ACTION_412_db_16"]),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x0c\x00\x01\x00\x00\x00\x04\x80'), identifier="ACTION_412_embedded_animation_routine_15"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=128, tiles=4, destinations=["ACTION_412_bpl_26_27_28_19"], identifier="ACTION_412_db_16"),
	Pause(48),
	Jmp(["ACTION_412_db_16"]),
	BPL262728(identifier="ACTION_412_bpl_26_27_28_19"),
	ClearSolidityBits(cant_pass_walls=True),
	SetPriority(3),
	Db(bytearray(b' \x07')),
	BPL2627(),
	VisibilityOn(),
	Db(bytearray(b'0\x00\x02')),
	Db(bytearray(b')\x00')),
	Pause(1, identifier="ACTION_412_pause_27"),
	Jmp(["ACTION_412_pause_27"])
])
