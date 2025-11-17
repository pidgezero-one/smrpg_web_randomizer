#A0786_EMPTY

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
	A_SetPriority(3),
	A_FixedFCoordOn(),
	A_WalkSoutheastSteps(2),
	A_FixedFCoordOff(),
	A_FaceSoutheast(),
	A_SetWalkingSpeed(FASTEST),
	A_SequencePlaybackOff(),
	A_FixedFCoordOn(),
	A_WalkSoutheastPixels(1, identifier="ACTION_786_shift_southeast_pixels_11"),
	A_WalkNorthwestPixels(1),
	A_Jmp(["ACTION_786_shift_southeast_pixels_11"])
])
