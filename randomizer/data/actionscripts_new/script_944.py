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
	SetWalkingSpeed(speed=NORMAL),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Db(bytearray(b'\xc8\x87')),
	SetVarToConst(Z_COORD_2, 13),
	WalkTo70167018701A(),
	WalkToXYCoords(x=3, y=82),
	SetBit(TEMP_7044_3),
	WalkToXYCoords(x=6, y=81),
	SetBit(TEMP_7044_4),
	WalkToXYCoords(x=7, y=82),
	Return()
])
