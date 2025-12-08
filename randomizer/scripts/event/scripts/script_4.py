# pylint: disable=C0301

"""E0004_LAUNCH_PROLOGUE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R002_BOWSERS_KEEP_OUTSIDE_MARIO_ENTERS_AT_BEGINNING_OF_GAME,
            face_direction=SOUTHWEST,
            x=7,
            y=18,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
