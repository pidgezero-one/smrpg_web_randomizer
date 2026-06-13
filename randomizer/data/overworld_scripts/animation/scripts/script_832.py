#A0832_CHAPEL_RING_PLACEMENT
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
    A_TransferToObjectXY(NPC_10),
    A_TransferXYZFPixels(x=0, y=12, z=14, direction=EAST),
    A_VisibilityOn(),
    A_SetPriority(3),
    A_JumpToHeight(height=152, silent=True),
    A_SetWalkingSpeed(VERY_FAST),
    A_WalkWestSteps(5),
    A_VisibilityOn(),
	A_Pause(1, identifier="ACTION_832_pause_8"),
	A_JmpIfBitClear(TEMP_7044_7, ["ACTION_832_pause_8"]),
    A_VisibilityOff(),
    A_ReturnQueue(),
])
