# pylint: disable=C0301

"""E1958_KEEP_ENTER_VERTICAL_PLATFORM_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
            face_direction=NORTHEAST,
            x=4,
            y=58,
            z=5),
        JmpToEvent(E1824_KEEP_SET_PLATFORM_PROPERTIES),
    ]
)
