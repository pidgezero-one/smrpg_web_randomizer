#A0830_CHAPEL_SHOES_PLACEMENT
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
    A_TransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
    A_SetPriority(3),
    A_VisibilityOn(),
    A_JumpToHeight(height=144, silent=True),
    A_ToggleSubroutineSlots(mask=0x03),
    A_SetSubroutineXTargets(slot_26_x=0xF600, slot_27_x=0xFD80),
    A_Pause(12),
    A_KillAllSubroutineSlots(),
    A_VisibilityOff(),
    A_ReturnQueue(),
])
