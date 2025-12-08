# pylint: disable=C0301

"""E0295_GO_TO_MUSHROOM_KINGDOM_OUTSIDE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R191_MUSHROOM_KINGDOM_OUTSIDE,
            face_direction=SOUTHWEST,
            x=12,
            y=82,
            z=9,
            run_entrance_event=True),
        Return(),
    ]
)
