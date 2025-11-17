#A0484_EMPTY

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
	A_JumpToHeight(64, identifier="ACTION_484_jump_to_height_0"),
	A_Pause(1, identifier="ACTION_484_pause_1"),
	A_JmpIfMarioInAir(["ACTION_484_pause_1"]),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_484_jump_to_height_0"]),
	A_ReturnQueue()
])
