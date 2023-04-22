# pylint: disable=C0301

"""E3739_NIMBUS_CASTLE_THRONE_ROOM_EXIT_TO_ANTECHAMBER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            face_direction=SOUTHWEST,
            x=3,
            y=121,
            z=3,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
