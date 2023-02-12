# referenced by monster_spells Boulder, monster_spells WaterBlast, monster_spells PetalBlast

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 8, script = [
	SetAMEMToRandom(amem=0x60, upper_bound=25),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352AEE),
	ReturnSubroutine()
])
