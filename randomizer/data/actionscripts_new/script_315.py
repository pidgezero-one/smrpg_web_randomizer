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
	ShadowOn(identifier="ACTION_315_shadow_on_0"),
	SetPriority(3),
	Pause(1),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_315_shadow_on_0"]),
	SetSpriteSequence(index=1, looping_off=True, is_sequence=True),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	Return()
])
