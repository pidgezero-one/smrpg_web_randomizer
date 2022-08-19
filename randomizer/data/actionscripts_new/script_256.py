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
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_256_reset_properties_8"]),
	ResetProperties(),
	FaceNortheast(),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	WalkToXYCoords(x=5, y=109),
	Return(),
	ResetProperties(identifier="ACTION_256_reset_properties_8"),
	FaceNortheast(),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	WalkToXYCoords(x=25, y=78),
	FaceNortheast(),
	Return()
])
