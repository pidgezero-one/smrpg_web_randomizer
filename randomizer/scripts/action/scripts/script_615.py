#A0615_MINES_PA_MOLE_ATTEMPTED_ESCAPE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitClear(MINES_BACK_OPENED, ["ACTION_615_visibility_off_3"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["ACTION_615_visibility_off_3"]),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	VisibilityOff(identifier="ACTION_615_visibility_off_3"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
