#A0118_PIPE_VAULT_CHOMPWEED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfRandom1of2(["ACTION_118_set_animation_speed_2"]),
	Pause(28),
	SetAllSpeeds(NORMAL, identifier="ACTION_118_set_animation_speed_2"),
	SequenceLoopingOn(),
	Return()
])
