# ENT0009_READY_TO_ATTACK

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SpriteSequence(sequence=5, looping_off=True),
	Db(bytearray(b'\x18\x00\x80')),
	SpriteSequence(sequence=5),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
