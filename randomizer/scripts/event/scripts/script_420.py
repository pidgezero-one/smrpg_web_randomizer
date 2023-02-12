# E0420_PIPE_VAULT_CROUCH_ROOM_EXIT_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES, face_direction=NORTHEAST, x=11, y=42, z=1, run_entrance_event=True),
	SetBit(TEMP_7044_5),
	Return()
])
