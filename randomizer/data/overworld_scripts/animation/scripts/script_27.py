#A0027_EMPTY

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
	A_FixedFCoordOff(identifier="ACTION_27_fixed_f_coord_off_0"),
	A_SetWalkingSpeed(VERY_FAST),
	A_WalkSouthwestSteps(2),
	A_WalkNortheastSteps(4),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_27_fixed_f_coord_off_0"])
])
