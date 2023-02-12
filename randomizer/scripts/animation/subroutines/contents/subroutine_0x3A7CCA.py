# referenced by battle_events BE0098_SMITHY_IS_DEFEATED

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 8, script = [
	SetAMEMToRandom(amem=0x60, upper_bound=25),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A7CD2),
	ReturnSubroutine()
])
