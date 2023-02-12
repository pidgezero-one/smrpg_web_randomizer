# E3864_WORLD_MAP_NIMBUS_LAND

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	EnterArea(room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, face_direction=SOUTH, x=28, y=27, z=2),
	RunEventAsSubroutine(E0282_UNKNOWN_PIPE_VAULT),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3864_ret_4"]),
	RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3864_ret_4")
])
