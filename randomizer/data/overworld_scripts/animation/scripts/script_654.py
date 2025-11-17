#A0654_EMPTY

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
	A_ShiftZUpPixels(1, identifier="ACTION_654_shift_z_up_pixels_0"),
	A_ShiftZDownPixels(1),
	A_Pause(16),
	A_StartLoopNTimes(1),
	A_ShiftZUpPixels(1),
	A_ShiftZDownPixels(1),
	A_EndLoop(),
	A_Pause(16),
	A_Jmp(["ACTION_654_shift_z_up_pixels_0"])
])
