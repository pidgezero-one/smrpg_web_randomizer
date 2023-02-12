#A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetAllSpeeds(NORMAL),
	OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SequencePlaybackOn(),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	SetVRAMPriority(NORMAL_PRIORITY),
	FloatingOn(),
	FixedFCoordOff(),
	ShadowOn(),
	ResetProperties(),
	SequenceLoopingOff(),
	Return()
])
