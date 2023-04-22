# pylint: disable=C0301

"""E0518_ROSE_TOWN_OCCUPIED_STAIRWAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
            face_direction=NORTHWEST,
            x=8,
            y=47,
            z=1,
            z_add_half_unit=True,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
