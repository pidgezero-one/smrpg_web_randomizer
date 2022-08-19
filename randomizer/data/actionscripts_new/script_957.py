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
	SetPriority(3),
	ShiftWestPixels(8),
	VisibilityOff(identifier="ACTION_957_visibility_off_2"),
	Pause(1),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_957_visibility_off_2"]),
	ClearBit(TEMP_7043_0),
	VisibilityOn(),
	SetSpriteSequence(index=0, looping_off=True),
	PlaySound(sound=S146_MACHINE_TRANSFORM, channel=4),
	Pause(36),
	Jmp(["ACTION_957_visibility_off_2"])
])
