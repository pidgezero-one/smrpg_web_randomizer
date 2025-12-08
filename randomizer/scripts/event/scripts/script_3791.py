# pylint: disable=C0301

"""E3791_OPEN_FACTORY_FINAL_BOSS_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R509_FACTORY_GROUNDS_SMITHYS_PAD,
            face_direction=NORTHEAST,
            x=4,
            y=11,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
