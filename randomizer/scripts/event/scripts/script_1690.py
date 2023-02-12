# E1690_TEMPLE_BOSS_ROOM_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM, face_direction=SOUTH, x=29, y=16, z=0),
	FadeInFromBlack(sync=True, identifier="EVENT_1690_fade_in_from_black_sync_2"),
	ClearBit(TEMP_707C_0),
	JmpToEvent(E0270_TRAMPOLINE_OR_PIPE_SUBROUTINE)
])
