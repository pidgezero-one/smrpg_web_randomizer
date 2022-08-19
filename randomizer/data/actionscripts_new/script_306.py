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
	SetSequenceSpeed(speed=VERY_SLOW),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_306_jmp_to_subroutine_5"]),
	Pause(80),
	JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_306_jmp_to_subroutine_5"),
	TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	Pause(40),
	Jmp(["ACTION_306_jmp_to_subroutine_5"]),
	VisibilityOn(identifier="ACTION_306_visibility_on_9"),
	SetSpriteSequence(index=1, is_sequence=True),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\xf0\xff\x00\x10\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x00\x04\x00\x01\xf8\xff\x00\x10\x80")),
	ShiftZDownSteps(5),
	BPL262728(),
	VisibilityOff(),
	Return()
])
