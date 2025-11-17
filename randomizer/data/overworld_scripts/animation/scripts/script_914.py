#A0914_EMPTY

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
	A_SetSpriteSequence(index=5, sprite_offset=3, is_sequence=True, looping=True),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	A_StartLoopNTimes(11),
	A_JmpIfMarioInAir(["ACTION_914_ret_6"]),
	A_Pause(1),
	A_EndLoop(),
	A_ReturnQueue(identifier="ACTION_914_ret_6")
])
