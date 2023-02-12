# E3926_TEMPLE_BACK_ENTRANCE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_3926_ret_26"]),
	EnterArea(room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, face_direction=SOUTHWEST, x=10, y=32, z=1, run_entrance_event=True),
	Return(identifier="EVENT_3926_ret_26")
])
