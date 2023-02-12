# E2468_BEAN_VALLEY_DEAD_END_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 17),
	SetVarToConst(Y_COORD_2, 85),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R252_BEAN_VALLEY_MAIN_AREA, face_direction=SOUTH, x=7, y=103, z=0, run_entrance_event=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
