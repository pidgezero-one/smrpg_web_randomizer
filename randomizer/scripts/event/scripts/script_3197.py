# E3197_MINES_FINAL_SAVE_ROOM_EXIT_TO_BOSS_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_3197_enter_area_0_"]),
	EnterArea(room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, face_direction=NORTHEAST, x=2, y=28, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, face_direction=NORTHEAST, x=2, y=28, z=0, run_entrance_event=True, identifier="EVENT_3197_enter_area_0_"),
	Return()
])
