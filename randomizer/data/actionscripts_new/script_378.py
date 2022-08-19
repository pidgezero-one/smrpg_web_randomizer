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
	SequenceLoopingOn(identifier="ACTION_378_sequence_looping_on_0"),
	SetSequenceSpeed(speed=SLOW),
	Pause(120),
	FaceSouthwest(),
	SetBit(TEMP_7043_1),
	Pause(120),
	ClearBit(TEMP_7043_1),
	FaceSoutheast(),
	JmpIfRandom1of2(["ACTION_378_sequence_looping_on_0"]),
	Pause(60),
	Jmp(["ACTION_378_sequence_looping_on_0"])
])
