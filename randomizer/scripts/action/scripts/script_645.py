#A0645_MIDAS_2ND_TUNNELS_JAWFUL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_645_clear_bit_13"]),
	Pause(1, identifier="ACTION_645_pause_2"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_645_pause_2"]),
	Pause(1, identifier="ACTION_645_pause_4"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_645_pause_4"]),
	Pause(109),
	StartLoopNTimes(1),
	Pause(32),
	SetSpriteSequence(index=3, looping=False),
	Pause(32),
	EndLoop(),
	Return(),
	ClearBit(MIDAS_RIVER_TUNNEL_1_BIT, identifier="ACTION_645_clear_bit_13"),
	Pause(168),
	SetSpriteSequence(index=3, looping=False),
	Pause(64),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_2, ["ACTION_645_pause_22"]),
	SetSpriteSequence(index=3, looping=False),
	Pause(35),
	SetBit(MIDAS_RIVER_TUNNEL_1_BIT),
	Return(),
	Pause(15, identifier="ACTION_645_pause_22"),
	SetSpriteSequence(index=3, looping=False),
	Pause(36),
	SetSequenceSpeed(SLOW),
	SetSpriteSequence(index=2, looping=False),
	Pause(50),
	FaceSoutheast(),
	Pause(40),
	SetSpriteSequence(index=4, looping=False, mirror_sprite=True),
	Return()
])
