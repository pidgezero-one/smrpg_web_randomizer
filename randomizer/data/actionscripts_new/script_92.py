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
	SetSequenceSpeed(speed=FAST),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_92_visibility_on_3"]),
	PlaySound(sound=S050_WATER_DROPLET, channel=4),
	VisibilityOn(identifier="ACTION_92_visibility_on_3"),
	SetSpriteSequence(index=10, is_sequence=True),
	Pause(10),
	SetSpriteSequence(index=1, is_sequence=True),
	Pause(5),
	SetWalkingSpeed(speed=FAST),
	ShiftNorthwestPixels(9),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNorthwestPixels(11),
	SetWalkingSpeed(speed=SLOW),
	ShiftNorthwestPixels(9),
	Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
