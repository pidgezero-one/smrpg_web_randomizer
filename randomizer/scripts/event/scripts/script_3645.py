# E3645_NIMBUS_EXTERIOR_EXIT_TO_VINES

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7049_0),
	EnterArea(room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, face_direction=SOUTH, x=24, y=18, z=2),
	JmpToEvent(E0282_UNKNOWN_PIPE_VAULT),
	Return()
])
