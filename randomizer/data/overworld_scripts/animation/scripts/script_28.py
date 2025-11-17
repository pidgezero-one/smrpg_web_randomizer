#A0028_EMPTY

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
	A_SetSpriteSequence(index=0, sprite_offset=2, is_mold=True, looping=True),
	A_FixedFCoordOn(),
	A_WalkNortheastPixels(4, identifier="ACTION_28_shift_northeast_pixels_2"),
	A_Pause(2),
	A_WalkSouthwestPixels(4),
	A_Jmp(["ACTION_28_shift_northeast_pixels_2"])
])
