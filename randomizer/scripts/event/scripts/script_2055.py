# E2055_MONSTRO_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN, face_direction=SOUTH, x=29, y=46, z=0, show_banner=True),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1584_TEMPLE_FINAL_ROOM_LOADER)
])
