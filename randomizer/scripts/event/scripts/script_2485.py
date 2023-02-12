# E2485_BEAN_VALLEY_LEFTMOST_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_2485_ret_5"]),
	SetVarToConst(X_COORD_2, 5),
	SetVarToConst(Y_COORD_2, 29),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, face_direction=SOUTH, x=3, y=49, z=0, run_entrance_event=True),
	Return(identifier="EVENT_2485_ret_5")
])
