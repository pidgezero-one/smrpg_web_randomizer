# E3162_MINES_AREA_2_LOWER_BACKWARD_EXIT_IF_MINES_CLEARED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["EVENT_3162_ret_2"]),
	EnterArea(room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, face_direction=SOUTHWEST, x=19, y=27, z=0, run_entrance_event=True),
	Return(identifier="EVENT_3162_ret_2")
])
