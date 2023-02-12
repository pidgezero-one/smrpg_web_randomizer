# referenced by ally_spells Super Jump, ally_spells Jump

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 66, script = [
	SetAMEM8BitTo7E1x(0x67, 0x7EE011, identifier="command_0x35c71f"),
	IncAMEM8Bit(0x67),
	JmpIfAMEM8BitLessThanConst(0x67, 2, ["command_0x35c746"]),
	Pause1Frame(),
	ClearAMEM8Bit(0x67),
	Set7E1xToAMEM8Bit(0x7EE011, 0x67),
	SetAMEM8BitTo7E1x(0x67, 0x7EE010),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x67, 125, ["command_0x35c74a"]),
	Pause1Frame(),
	IncAMEM8Bit(0x67),
	Set7E1xToAMEM8Bit(0x7EE010, 0x67),
	Jmp(["command_0x35c74a"]),
	Set7E1xToAMEM8Bit(0x7EE011, 0x67, identifier="command_0x35c746"),
	ReturnSubroutine(identifier="command_0x35c74a"),
	Pause1Frame(identifier="command_0x35c74b"),
	SetAMEM8BitTo7E1x(0x67, 0x7EE013),
	JmpIfAMEM8BitGreaterOrEqualThanAMEM(amem=0x67, source_amem=0xCB, destinations=["command_0x35c760"]),
	JmpIfAMEM8BitGreaterOrEqualThanConst(0x67, 100, ["command_0x35c760"]),
	Set7E1xToAMEM8Bit(0x7EE013, 0x6B),
	ReturnSubroutine(identifier="command_0x35c760")
])
