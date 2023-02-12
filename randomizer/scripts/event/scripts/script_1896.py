# E1896_ABYSS_AXEM_PIT_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(ABYSS_FINAL_ROOM_TRAMPOLINE),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, face_direction=SOUTH, x=8, y=35, z=5, run_entrance_event=True),
	Return()
])
