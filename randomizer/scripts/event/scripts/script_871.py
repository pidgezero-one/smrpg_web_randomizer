# pylint: disable=C0301

"""E0871_TEST_SCRIPT_5"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R000_DEBUG_ROOM,
            face_direction=SOUTHEAST,
            x=7,
            y=24,
            z=5,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
