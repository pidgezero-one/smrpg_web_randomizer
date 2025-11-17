#A0558_EMPTY

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
	A_VisibilityOff(identifier="ACTION_558_visibility_off_0"),
	A_SequenceLoopingOn(),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 112),
	A_AddConstToVar(PRIMARY_TEMP_700C, 32),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 36, ["ACTION_558_visibility_on_10"]),
	A_SetPriority(3),
	A_VisibilityOn(identifier="ACTION_558_visibility_on_10"),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
	A_ShadowOn(),
	A_PlaySound(sound=SO084_SMOKED, channel=4),
	A_Pause(8),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x0cp\xff')),
	A_Pause(25),
	A_BPL262728(),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_StartLoopNTimes(2),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_EndLoop(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 18),
	A_AddConstToVar(PRIMARY_TEMP_700C, 8),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x00\x80\xff')),
	A_Pause(21),
	A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
	A_Pause(5),
	A_Jmp(["ACTION_558_visibility_off_0"])
])
