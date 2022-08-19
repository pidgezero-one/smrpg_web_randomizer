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
	Set700CToPressedButton(identifier="ACTION_712_set_700C_to_pressed_button_0"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_712_pause_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 29, ["ACTION_712_db_7"]),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\x00\x00\x00\x02\x80")),
	Return(),
	Db(bytearray(b' \x03'), identifier="ACTION_712_db_7"),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00 \x00\x01\x00\x00\x80\x01\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x80\x01\x80")),
	Return(),
	Pause(2, identifier="ACTION_712_pause_11"),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80")),
	Return()
])
