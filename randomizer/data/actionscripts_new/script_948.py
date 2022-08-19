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
	ShadowOff(identifier="ACTION_948_shadow_off_0"),
	SetWalkingSpeed(speed=SLOW),
	WalkToXYCoords(x=11, y=38),
	ShiftSoutheastPixels(11),
	SetBit(TEMP_7043_0),
	WalkToXYCoords(x=11, y=39),
	VisibilityOff(),
	WalkToXYCoords(x=16, y=49),
	ShiftToXYCoords(x=3, y=88),
	ShiftSoutheastSteps(3),
	ShiftToXYCoords(x=6, y=28),
	VisibilityOn(),
	Jmp(["ACTION_948_shadow_off_0"])
])
