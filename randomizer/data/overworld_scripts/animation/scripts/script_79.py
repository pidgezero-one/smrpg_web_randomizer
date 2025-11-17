#A0079_EMPTY

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
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_FloatingOn(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_JumpToHeight(height=64, silent=True, identifier="ACTION_79_jump_to_height_silent_3"),
	A_Pause(1, identifier="ACTION_79_pause_4"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_79_pause_4"]),
	A_Jmp(["ACTION_79_jump_to_height_silent_3"])
])
