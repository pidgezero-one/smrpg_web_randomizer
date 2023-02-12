# E3116_CHANGE_MUSIC_IN_MOLEVILLE_MINES_WHEN_BACKTRACKING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_3116_ret_3"]),
	FadeOutToBlack(sync=False),
	PlayMusicAtDefaultVolume(M33_MOLEVILLE),
	Return(identifier="EVENT_3116_ret_3")
])
