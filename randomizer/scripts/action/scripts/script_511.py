#A0511_PIPE_VAULT_3_CHEST_ROOM_COIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	SetSequenceSpeed(SLOW),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	SetPriority(3),
	Return()
])
