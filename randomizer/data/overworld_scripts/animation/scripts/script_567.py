#A0567_EMPTY

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_ClearBit(TEMP_7043_6),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(10),
	A_SetWalkingSpeed(FAST),
	A_WalkNortheastPixels(16),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNortheastPixels(5),
	A_SetWalkingSpeed(SLOW),
	A_WalkNortheastPixels(2),
	A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(10),
	A_VisibilityOff(),
	A_ReturnQueue()
])
