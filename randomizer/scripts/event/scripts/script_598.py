# E0598_MINES_INITIATE_FINAL_BOSS_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	InitiateBattleMask(),
	EnterArea(room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, face_direction=NORTHEAST, x=6, y=19, z=0, run_entrance_event=True),
	Return()
])
