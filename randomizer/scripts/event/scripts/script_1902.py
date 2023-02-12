# E1902_ABYSS_EXIT_TO_SIDE_TREASURE_ROOMS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM, face_direction=NORTHEAST, x=20, y=25, z=0, run_entrance_event=True),
	Return()
])
