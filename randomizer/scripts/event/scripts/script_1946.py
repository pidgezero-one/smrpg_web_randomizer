# pylint: disable=C0301

"""E1946_KEEP_DONKEY_ROOM_EXIT_TO_PREVIOUS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            face_direction=SOUTHWEST,
            x=20,
            y=88,
            z=2,
        ),
        JmpToEvent(E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER),
    ]
)
