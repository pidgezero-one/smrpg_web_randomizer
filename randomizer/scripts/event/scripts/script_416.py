# E0416_PIPE_VAULT_THWOMP_ROOM_ENTRANCE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R123_PIPE_VAULT_AREA_01, face_direction=SOUTHWEST, x=11, y=8, z=1, run_entrance_event=True),
	Return()
])
