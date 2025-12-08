# pylint: disable=C0301

"""E1960_KEEP_ENTER_INVISIBLE_FLOOR_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            face_direction=NORTHEAST,
            x=8,
            y=115,
            z=2),
        JmpToEvent(E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER),
    ]
)
