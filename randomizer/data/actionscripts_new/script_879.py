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
	Pause(3, identifier="ACTION_879_pause_0"),
	JmpIfRandom1of2(["ACTION_879_pause_0"]),
	Set700CToObjectCoord(object=NPC_1, coord=F, pixel=True),
	FaceEast7C(),
	Pause(1),
	Jmp(["ACTION_879_pause_0"])
])
