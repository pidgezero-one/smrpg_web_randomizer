# E0192_GATING_AND_PARTY_JOIN_LOGIC

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0013_BASE_ROM_ONLY_FIX_MAP_AND_PARTY),
	EnterArea(room_id=R189_MARIOS_PIPEHOUSE, face_direction=SOUTHEAST, x=3, y=13, z=0),
	JmpToEvent(E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING)
])
