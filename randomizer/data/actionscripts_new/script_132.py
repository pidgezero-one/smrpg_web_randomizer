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
	SetPriority(3, identifier="ACTION_132_set_priority_0"),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x07\xa0\xff')),
	SetWalkingSpeed(speed=SLOW),
	ShiftNorthwestPixels(16),
	BPL262728(),
	FaceSoutheast(),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x04\xa0\xff')),
	ShiftSoutheastPixels(16),
	BPL262728(),
	Jmp(["ACTION_132_set_priority_0"])
])
