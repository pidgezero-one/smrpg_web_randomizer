#A0781_PLAYER_SPINS_ON_FLOWER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitSet(SPINNING_FLOWER_1, ["ACTION_781_play_sound_12"]),
	SetBit(TEMP_7043_0),
	ClearSolidityBits(cant_pass_walls=True),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetVRAMPriority(PRIORITY_3),
	Db(bytearray(b'\xc8\x91')),
	SetWalkingSpeed(SLOW),
	RunAwayShift(),
	SetWalkingSpeed(NORMAL),
	SetVRAMPriority(NORMAL_PRIORITY),
	ClearBit(TEMP_7043_0),
	Return(),
	PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4, identifier="ACTION_781_play_sound_12"),
	JumpToHeight(height=48, silent=True),
	RunAwayShift(),
	Return()
])
