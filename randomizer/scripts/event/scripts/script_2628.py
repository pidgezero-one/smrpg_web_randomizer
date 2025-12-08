# pylint: disable=C0301

"""E2628_ENDING_CREDITS_SUNSET_OPENER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
            face_direction=NORTHWEST,
            x=0,
            y=0,
            z=0),
        JmpToEvent(E2619_ENDING_CREDITS_SUNSET),
        Return(),
    ]
)
