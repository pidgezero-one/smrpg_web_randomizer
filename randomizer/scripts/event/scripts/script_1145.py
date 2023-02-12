# E1145_SEASIDE_OCCUPIED_BEACH_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["EVENT_1146_action_queue_sync_2"]),
	FadeInFromBlack(sync=False),
	Return()
])
