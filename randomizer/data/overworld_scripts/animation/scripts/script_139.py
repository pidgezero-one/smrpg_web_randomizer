#A0139_EMPTY

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
	A_PlaySound(sound=SO047_SNOOZE, channel=6, identifier="ACTION_139_play_sound_0"),
	A_SetSpriteSequence(index=27, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(32),
	A_SetSpriteSequence(index=28, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(16),
	A_SetSpriteSequence(index=29, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(16),
	A_Jmp(["ACTION_139_play_sound_0"])
])
