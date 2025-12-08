# pylint: disable=C0301

"""E0673_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_ANTECHAMBER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            face_direction=NORTHEAST,
            x=18,
            y=20,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
