# pylint: disable=C0301

"""E1878_KEEP_CANNONBALL_ROOM_EXIT_TO_PREVIOUS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
            face_direction=SOUTHWEST,
            x=18,
            y=30,
            z=5,
        ),
        SetBit(TEMP_7044_6),
        JmpToEvent(E1824_KEEP_SET_PLATFORM_PROPERTIES),
    ]
)
