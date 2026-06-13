#A0833_CHAPEL_CROWN_PLACEMENT
# pyright: reportWildcardImportFromLibrary=false

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
    A_TransferToObjectXYZ(NPC_9),
    A_ShiftZUpSteps(2, identifier="crown_adjust_height"),
    A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True, cant_pass_npcs=True),
    A_Pause(1, identifier="ACTION_833_pause_8"),
	A_Jmp(["ACTION_833_pause_8"]),
])
