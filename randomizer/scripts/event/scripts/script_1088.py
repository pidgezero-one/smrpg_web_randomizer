# E1088_MELODY_BAY_THIRD_SONG_HINT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO038_TADPOLE_POND_STAFF_MI, channel=6),
	Pause(45),
	PlaySound(sound=SO039_TADPOLE_POND_STAFF_FA, channel=6),
	Pause(45),
	PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6),
	Pause(45),
	PlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=6),
	Pause(75),
	PlaySound(sound=SO037_TADPOLE_POND_STAFF_RE, channel=6),
	Pause(100),
	Return()
])
