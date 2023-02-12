# E0669_ENTER_UNOCCUPIED_MARRYMORE_SANCTUARY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True),
	Return()
])
