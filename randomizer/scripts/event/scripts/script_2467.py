# E2467_BEAN_VALLEY_PIPE_TO_DEAD_END

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 7),
	SetVarToConst(Y_COORD_2, 103),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R252_BEAN_VALLEY_MAIN_AREA, face_direction=SOUTH, x=17, y=85, z=0, run_entrance_event=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
