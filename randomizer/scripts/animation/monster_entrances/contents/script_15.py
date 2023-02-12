# ENT0015_READY_TO_ATTACK

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetAMEM8BitTo7E1x(0x68, 0x7EE00C),
	IncAMEM8Bit(0x68),
	Set7E1xToAMEM8Bit(0x7EE00C, 0x68),
	Set7E5xToAMEM8Bit(0x7E0064, 0x68),
	SpriteSequence(sequence=5, looping_off=True),
	Db(bytearray(b'\x18\x00\x80')),
	SpriteSequence(sequence=5),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
