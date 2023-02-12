# E2484_BEAN_VALLEY_TOP_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_2484_ret_5"]),
	SetVarToConst(X_COORD_2, 7),
	SetVarToConst(Y_COORD_2, 25),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, face_direction=SOUTH, x=19, y=47, z=0, run_entrance_event=True),
	Return(identifier="EVENT_2484_ret_5")
])
