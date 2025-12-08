# pylint: disable=C0301

"""E2070_MONSTROMAMA_HOUSE_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R324_MONSTRO_TOWN_OUTSIDE,
            face_direction=SOUTHWEST,
            x=7,
            y=54,
            z=4,
            run_entrance_event=True),
        Return(),
    ]
)
