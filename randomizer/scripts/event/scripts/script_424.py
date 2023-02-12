# E0424_PIPE_VAULT_RED_ROOM_ENTRANCE_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 2),
	SetVarToConst(Y_COORD_2, 100),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R129_PIPE_VAULT_AREA_05, face_direction=SOUTHWEST, x=25, y=100, z=1, run_entrance_event=True),
	JmpToEvent(E0269_PIPE_UP_SUBROUTINE)
])
