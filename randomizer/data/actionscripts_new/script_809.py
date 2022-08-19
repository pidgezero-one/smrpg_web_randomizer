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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_809_db_6"]),
	Db(bytearray(b' \x03')),
	Db(bytearray(b'$\x00\xfe\x00\x01')),
	Pause(1, identifier="ACTION_809_pause_4"),
	Jmp(["ACTION_809_pause_4"]),
	Db(bytearray(b' \x03'), identifier="ACTION_809_db_6"),
	Db(bytearray(b'$\x00\x02\x00\x01')),
	Jmp(["ACTION_809_pause_4"])
])
