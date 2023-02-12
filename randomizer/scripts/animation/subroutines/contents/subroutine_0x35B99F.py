# referenced by ally_spells Geno Beam

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 9, script = [
	SetAMEM16BitToConst(0x60, 0, identifier="queuestart_0x35b99f"),
	ObjectQueueAtOffsetAndIndex(index=26, target_address=0x35B43D),
	ReturnSubroutine()
])
