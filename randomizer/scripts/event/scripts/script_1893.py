# E1893_ABYSS_BOSS_2_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(ABYSS_BOSS_2_DEFEATED, ["EVENT_1893_fade_in_from_black_async_3"]),
	RunEventAtReturn(E1894_ABYSS_BOSS_2),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_1893_fade_in_from_black_async_3"),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 5),
	Return()
])
