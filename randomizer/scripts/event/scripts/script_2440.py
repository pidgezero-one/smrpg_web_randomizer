# E2440_FOREST_FINAL_WIGGLER_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7047_1),
	SetVarToConst(X_COORD_2, 20),
	SetVarToConst(Y_COORD_2, 108),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, face_direction=SOUTH, x=3, y=33, z=0, run_entrance_event=True),
	Return()
])
