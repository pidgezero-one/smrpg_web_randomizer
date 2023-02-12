# E0128_ABORT_ATTRACT_MODE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StopMusic(),
	StopMusicFD9F(),
	StopMusicFDA0(),
	StopMusicFDA1(),
	StopMusicFDA2(),
	StopMusicFDA6(),
	Return()
])
