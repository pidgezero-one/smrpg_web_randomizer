# E0422_PIPE_VAULT_PLATFORMING_ROOM_ENTRANCE_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 12),
	SetVarToConst(Y_COORD_2, 126),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES, face_direction=SOUTHWEST, x=15, y=34, z=1, run_entrance_event=True),
	Return()
])
