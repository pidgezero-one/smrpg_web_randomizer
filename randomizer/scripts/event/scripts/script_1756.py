# E1756_LANDS_END_SHY_AWAY_WHIRLPOOL_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL),
	EnterArea(room_id=R318_LANDS_END_DESERT_AREA_02, face_direction=SOUTH, x=12, y=58, z=0),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	SetVarToConst(ACTIVE_NPC, 24),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1787_LANDS_END_DESERT_1_RIGHT_WHIRLPOOL_SUBROUTINE)
])
