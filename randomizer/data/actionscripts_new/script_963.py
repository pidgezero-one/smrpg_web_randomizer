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
	ShadowOff(),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthwestPixels(6),
	Pause(1, identifier="ACTION_963_pause_3"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_963_pause_3"]),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(32),
	SetBit(TEMP_7043_4),
	Pause(4),
	ClearBit(TEMP_7043_1),
	Jmp(["ACTION_963_pause_3"])
])
