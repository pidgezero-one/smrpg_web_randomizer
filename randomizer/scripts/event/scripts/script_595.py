# pylint: disable=C0301

"""E0595_MINES_BOSS_ROOM_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            face_direction=NORTHEAST,
            x=3,
            y=59,
            z=2,
            run_entrance_event=True),
        Return(),
    ]
)
