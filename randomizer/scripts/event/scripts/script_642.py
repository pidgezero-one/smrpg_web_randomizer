# pylint: disable=C0301

"""E0642_MARRYMORE_ANTECHAMBER_ENTRANCE_REVERSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL,
            face_direction=SOUTHWEST,
            x=6,
            y=27,
            z=3,
            z_add_half_unit=True,
            run_entrance_event=True),
        Return(),
    ]
)
