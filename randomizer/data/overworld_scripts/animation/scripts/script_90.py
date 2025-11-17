#A0090_EMPTY

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
	A_Pause(70),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_FixedFCoordOn(),
	A_SetSequenceSpeed(FAST),
	A_SequenceLoopingOn(),
	A_StartLoopNTimes(6),
	A_SetWalkingSpeed(SLOW),
	A_WalkWestPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNorthwestPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSoutheastPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkEastPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(SLOW),
	A_WalkEastPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkNortheastPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(1),
	A_Pause(1),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkWestPixels(1),
	A_Pause(1),
	A_EndLoop(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
