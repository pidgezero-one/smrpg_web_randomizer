# pylint: disable=C0301

"""E1943_KEEP_INVISIBLE_FLOOR_ROOM_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            face_direction=NORTHEAST,
            x=7,
            y=117,
            z=2,
        ),
        JmpToEvent(E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER),
    ]
)
