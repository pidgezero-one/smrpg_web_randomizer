# E1760_LANDS_END_STAGE_2_WHIRLPOOL_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL),
	EnterArea(room_id=R402_LANDS_END_DESERT_AREA_03, face_direction=SOUTH, x=24, y=22, z=0),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	SetVarToConst(ACTIVE_NPC, 23),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1784_LANDS_END_DESERT_1_LEFT_WHIRLPOOL_SUBROUTINE)
])
