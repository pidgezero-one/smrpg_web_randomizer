# E3785_BEAN_VALLEY_1ST_VINE_ROOM_EXIT_TO_GROUND_LEVEL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA, face_direction=SOUTH, x=27, y=27, z=0, run_entrance_event=True),
	Return()
])
