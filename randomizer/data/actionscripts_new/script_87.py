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
	SetBit(TEMP_7043_5),
	ShiftToXYCoords(x=3, y=40),
	VisibilityOn(),
	SetSequenceSpeed(speed=FAST),
	PlaySound(sound=S050_WATER_DROPLET, channel=4),
	SetSpriteSequence(index=10, is_sequence=True),
	Pause(12),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	SetWalkingSpeed(speed=FAST),
	ShiftSoutheastSteps(1),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSoutheastPixels(8),
	SetWalkingSpeed(speed=SLOW),
	ShiftSoutheastPixels(5),
	Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
