# referenced by 

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 8, script = [
	SetAMEMToRandom(amem=0x60, upper_bound=9),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A79A1),
	ReturnSubroutine()
])
