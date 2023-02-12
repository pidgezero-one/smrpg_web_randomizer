# E3213_SHIP_POST_1ST_BOSS_TRAMPOLINE_BACK_UP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, face_direction=SOUTHWEST, x=15, y=43, z=0, run_entrance_event=True),
	Return()
])
