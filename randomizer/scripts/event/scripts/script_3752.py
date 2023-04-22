# pylint: disable=C0301

"""E3752_HOT_SPRINGS_EXIT_TO_LOBBY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS,
            face_direction=NORTHWEST,
            x=20,
            y=56,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
