# pylint: disable=C0301

"""E2568_BOOSTER_PASS_EXIT_TO_SECRET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(BOOSTER_PASS_SECRET_OPEN, ["EVENT_2568_ret_2"]),
        EnterArea(
            room_id=R405_BOOSTER_PASS_SECRET,
            face_direction=NORTHWEST,
            x=22,
            y=74,
            z=15,
            run_entrance_event=True),
        Return(identifier="EVENT_2568_ret_2"),
    ]
)
