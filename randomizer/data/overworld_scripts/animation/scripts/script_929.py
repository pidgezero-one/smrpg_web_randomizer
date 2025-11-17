#A0929_EMPTY

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
	A_SetBit(TEMP_7044_6),
	A_JmpIfVarEqualsConst(TEMP_70AF, 6, ["ACTION_929_play_sound_7"]),
	A_JmpIfVarEqualsConst(TEMP_70AF, 7, ["ACTION_929_set_sprite_sequence_10"]),
	A_JmpIfVarEqualsConst(TEMP_70AF, 135, ["ACTION_929_set_sprite_sequence_12"]),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=False, mirror_sprite=True),
	A_Jmp(["ACTION_929_pause_14"]),
	A_PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4, identifier="ACTION_929_play_sound_7"),
	A_SetSpriteSequence(index=6, is_sequence=True, looping=False),
	A_Jmp(["ACTION_929_pause_14"]),
	A_SetSpriteSequence(index=7, is_sequence=True, looping=False, identifier="ACTION_929_set_sprite_sequence_10"),
	A_Jmp(["ACTION_929_pause_14"]),
	A_SetSpriteSequence(index=7, is_sequence=True, looping=False, mirror_sprite=True, identifier="ACTION_929_set_sprite_sequence_12"),
	A_Jmp(["ACTION_929_pause_14"]),
	A_Pause(1, identifier="ACTION_929_pause_14"),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_929_pause_14"]),
	A_Pause(1),
	A_ReturnQueue()
])
