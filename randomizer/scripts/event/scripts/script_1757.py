# E1757_LANDS_END_SHY_AWAY_WHIRLPOOL_3

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL),
	EnterArea(room_id=R317_LANDS_END_DESERT_AREA_01, face_direction=SOUTH, x=9, y=17, z=0),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	SetVarToConst(ACTIVE_NPC, 22),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1782_LANDS_END_DESERT_1_LOADER)
])
