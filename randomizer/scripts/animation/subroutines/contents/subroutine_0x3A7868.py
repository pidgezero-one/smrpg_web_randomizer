# referenced by battle_events BE0079_MAGIKOOPA_SUMMONS_MONSTER, battle_events BE0092_SHELLY_BREAKS, battle_events BE0044_CZAR_DRAGON_DIES

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 30, script = [
	Pause1Frame(identifier="command_0x3a7868"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01C),
	JmpIfAMEMBitsClear(0x68, [6], ["command_0x3a7868"]),
	ReturnSubroutine(),
	Pause1Frame(identifier="command_0x3a7873"),
	SetAMEM8BitTo7E1x(0x68, 0x7EE01C),
	JmpIfAMEMBitsClear(0x68, [7], ["command_0x3a7873"]),
	ReturnSubroutine(),
	SetAMEMToRandom(amem=0x60, upper_bound=25),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A7886),
	ReturnSubroutine()
])
