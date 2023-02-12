#A0184_CHEST_SLOT_MACHINE_ROLLER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	SetVarToConst(FACTORY_FALL_1, 1, identifier="ACTION_184_set_2"),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Pause(9),
	SetVarToConst(FACTORY_FALL_1, 0),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(9),
	SetVarToConst(FACTORY_FALL_1, 2),
	SetSpriteSequence(index=3, is_sequence=True, looping=True),
	Pause(9),
	Jmp(["ACTION_184_set_2"])
])
