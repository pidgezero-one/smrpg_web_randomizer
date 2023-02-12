# E2651_BUCKET_WARP_CHECK_GRANTER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(EXP_STAR_70D5, 6, ["EVENT_2651_summon_to_level_51"]),
	SetBit(BUCKET_WARP_BIT),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=108, z=0, run_entrance_event=True),
	Return(),
	JmpToEvent(E3791_OPEN_FACTORY_FINAL_BOSS_ROOM, identifier="EVENT_2651_summon_to_level_51"),
	Return()
])
