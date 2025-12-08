# pylint: disable=C0301

"""E0349_MUSHROOM_KINGDOM_ANTECHAMBER_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
            face_direction=NORTHEAST,
            x=13,
            y=35,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
