# pylint: disable=C0301

"""E2629_ENDING_CREDITS_KEEP_OPENER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER__TROOPS_REPAIR,
            face_direction=NORTHWEST,
            x=0,
            y=0,
            z=0),
        JmpToEvent(E2622_ENDING_CREDITS_KEEP),
        Return(),
    ]
)
