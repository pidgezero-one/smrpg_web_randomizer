# pylint: disable=C0301

"""E3765_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_LOWER_CHEST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD,
            face_direction=SOUTH,
            x=27,
            y=91,
            z=4),
        RunEventAsSubroutine(E3763_NIMBUS_BACK_EXIT_MARIO_FALL_ANIMATION),
        Return(),
    ]
)
