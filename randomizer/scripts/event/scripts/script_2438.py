# E2438_FOREST_SECRET_TRUNK

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7047_1),
	SetVarToConst(X_COORD_2, 19),
	SetVarToConst(Y_COORD_2, 74),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R234_FOREST_MAZE_SECRET, face_direction=SOUTH, x=10, y=84, z=0, run_entrance_event=True),
	Return()
])
