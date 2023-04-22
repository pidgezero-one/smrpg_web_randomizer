# pylint: disable=C0301

"""E1935_KEEP_ROTATING_ROOM_EXIT_TO_PREVIOUS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            face_direction=SOUTHWEST,
            x=17,
            y=29,
            z=3,
        ),
        JmpToEvent(E1835_KEEP_CANNONBALL_ROOM_LOADER),
    ]
)
