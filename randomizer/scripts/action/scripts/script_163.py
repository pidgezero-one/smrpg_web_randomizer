#A0163_MIDAS_SMALL_COIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Set700CToCurrentLevel(identifier="ACTION_163_set_700C_to_current_level_0"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 422, ["ACTION_163_shadow_on_3"]),
	SetVRAMPriority(PRIORITY_3),
	ShadowOn(identifier="ACTION_163_shadow_on_3"),
	SetPriority(3),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	SequenceLoopingOn(),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Return()
])
