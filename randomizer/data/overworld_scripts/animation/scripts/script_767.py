#A0767_EMPTY

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
	A_WalkNortheastPixels(8),
	A_ShadowOff(),
	A_SequencePlaybackOff(),
	A_FloatingOn(),
	A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x00\x80\xff')),
	A_Pause(40),
	A_BPL262728(),
	A_SetSpriteSequence(index=14, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=15, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=16, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(2),
	A_SetSpriteSequence(index=15, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue()
])
