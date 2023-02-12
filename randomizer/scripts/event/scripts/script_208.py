# E0208_UNLOCK_KEEP_IF_GATED_BY_VOLCANO_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(KEEP_GATED_BY_VOLCANO, ["EVENT_208_ret"]),
	SetBit(MAP_VISTA_HILL),
	ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
	JmpToEvent(E3093_OPEN_ABYSS_IF_STAR_PIECE_THRESHOLD_MET, identifier="EVENT_208_ret")
])
