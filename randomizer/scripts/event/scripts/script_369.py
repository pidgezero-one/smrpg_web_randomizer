# pylint: disable=C0301

"""E0369_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            ["EVENT_369_ret_1"]),
        EnterArea(
            room_id=R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
            face_direction=SOUTHWEST,
            x=28,
            y=93,
            z=0,
            run_entrance_event=True),
        Return(identifier="EVENT_369_ret_1"),
    ]
)
