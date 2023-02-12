#A0617_MINES_LEFT_CROOK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitSet(MINES_HENCHMAN_LEFT_DEFEATED, ["ACTION_617_visibility_off_10"]),
	JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_617_visibility_off_10"]),
	Return(),
	VisibilityOff(identifier="ACTION_617_visibility_off_10"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SequencePlaybackOff(),
	Return()
])
