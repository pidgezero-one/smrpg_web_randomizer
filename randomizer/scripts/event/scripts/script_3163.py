# E3163_SEWERS_TUTORIAL_ROOM_EXIT_TO_EXTERIOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 5),
	SetVarToConst(Y_COORD_2, 90),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R333_KERO_SEWERS_ENTRANCE, face_direction=SOUTH, x=5, y=20, z=0, run_entrance_event=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
