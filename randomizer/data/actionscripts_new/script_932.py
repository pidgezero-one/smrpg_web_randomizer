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
	TransferXYZFPixels(x=0, y=0, z=0, direction=EAST, identifier="ACTION_932_transfer_xyzf_pixels_0"),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(2, identifier="ACTION_932_pause_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_932_pause_2"]),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(60),
	SetSpriteSequence(index=1, is_sequence=True),
	Pause(8),
	Jmp(["ACTION_932_transfer_xyzf_pixels_0"])
])
