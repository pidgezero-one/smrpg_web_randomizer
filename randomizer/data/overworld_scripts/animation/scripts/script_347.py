#A0347_EMPTY

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
	A_VisibilityOff(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_TransferToObjectXY(NPC_1),
	A_TransferXYZFPixels(x=0, y=0, z=8, direction=NORTHEAST),
	A_JmpIfVarEqualsConst(TEMP_7032, 1, ["ACTION_347_pause_13"]),
	A_Pause(7),
	A_VisibilityOn(),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(6),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_Pause(1, identifier="ACTION_347_pause_13"),
	A_JmpIfVarNotEqualsConst(TEMP_7032, 1, ["ACTION_347_pause_13"]),
	A_TransferToObjectXY(NPC_1),
	A_TransferXYZFPixels(x=0, y=0, z=8, direction=NORTHEAST),
	A_VisibilityOn(),
	A_Pause(42),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpSteps(3),
	A_ShiftZUpPixels(2),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZUpPixels(6),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(4),
	A_Pause(1, identifier="ACTION_347_pause_26"),
	A_JmpIfVarNotEqualsConst(TEMP_7032, 2, ["ACTION_347_pause_26"]),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpSteps(8),
	A_VisibilityOff(),
	A_ReturnQueue()
])
