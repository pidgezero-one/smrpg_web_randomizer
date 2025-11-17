#A0017_EMPTY

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
	A_SetWalkingSpeed(FASTEST),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkNorthwestPixels(1, identifier="ACTION_17_shift_northwest_pixels_2"),
	A_WalkSoutheastPixels(2),
	A_WalkNorthwestPixels(1),
	A_StartLoopNTimes(29),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_17_face_southeast_10"]),
	A_Pause(1),
	A_EndLoop(),
	A_Jmp(["ACTION_17_shift_northwest_pixels_2"]),
	A_FaceSoutheast(identifier="ACTION_17_face_southeast_10"),
	A_SetWalkingSpeed(NORMAL),
	A_ResetProperties(),
	A_ReturnQueue()
])
