#A0297_EMPTY

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
	A_StartLoopNTimes(10),
	A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(4),
	A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(4),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(8),
	A_EndLoop(),
	A_ResetProperties(),
	A_ReturnQueue()
])
