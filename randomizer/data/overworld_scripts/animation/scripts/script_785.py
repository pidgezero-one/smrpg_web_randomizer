#A0785_EMPTY

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
	A_SetWalkingSpeed(VERY_FAST),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_FloatingOff(),
	A_SetPriority(2),
	A_FixedFCoordOn(),
	A_WalkNorthwestSteps(1),
	A_FixedFCoordOff(),
	A_WalkNortheastSteps(2),
	A_SetWalkingSpeed(FASTEST),
	A_SequencePlaybackOff(),
	A_FixedFCoordOn(),
	A_WalkNortheastPixels(1, identifier="ACTION_785_shift_northeast_pixels_11"),
	A_WalkSouthwestPixels(1),
	A_Jmp(["ACTION_785_shift_northeast_pixels_11"])
])
