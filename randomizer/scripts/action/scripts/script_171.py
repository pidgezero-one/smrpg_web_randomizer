#A0171_MINIGAME_COIN_SPINS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	SequenceLoopingOn(),
	JmpIfBitSet(MINECART_INITIATE_FREEPLAY, ["ACTION_171_set_animation_speed_11"]),
	SetWalkingSpeed(FAST),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	JumpToHeight(80),
	FaceEast7C(),
	ShiftFDirectionPixels(48),
	VisibilityOff(),
	Return(),
	SetWalkingSpeed(NORMAL, identifier="ACTION_171_set_animation_speed_11"),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	JumpToHeight(96),
	ShiftSoutheastPixels(17),
	VisibilityOff(),
	Return()
])
