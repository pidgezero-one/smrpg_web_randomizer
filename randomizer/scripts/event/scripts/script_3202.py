# pylint: disable=C0301

"""E3202_MINECART_ROOM_EXIT_TO_BOSS_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            face_direction=SOUTHWEST,
            x=8,
            y=15,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
