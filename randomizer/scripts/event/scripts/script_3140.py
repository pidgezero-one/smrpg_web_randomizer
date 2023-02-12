# E3140_1ST_WATER_TOOM_PIPE_TO_SEWERS_4_RAT_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(X_COORD_2, 14),
	SetVarToConst(Y_COORD_2, 30),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS, face_direction=SOUTH, x=20, y=100, z=0, run_entrance_event=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
