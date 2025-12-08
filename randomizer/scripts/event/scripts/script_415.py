# pylint: disable=C0301

"""E0415_PIPE_VAULT_ROOM_1_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R127_PIPE_VAULT_AREA_02,
            face_direction=NORTHEAST,
            x=17,
            y=44,
            z=1,
            run_entrance_event=True),
        Return(),
    ]
)
