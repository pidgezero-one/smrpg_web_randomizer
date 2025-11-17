#A0669_EMPTY

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
	A_ShadowOn(identifier="ACTION_669_shadow_on_0"),
	A_VisibilityOn(),
	A_SetPriority(3),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_AddZCoord1Step(),
	A_ShiftZUpPixels(12),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(48),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_DecZCoord1Step(),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ShiftZDownPixels(12),
	A_VisibilityOff(),
	A_Jmp(["ACTION_669_shadow_on_0"])
])
