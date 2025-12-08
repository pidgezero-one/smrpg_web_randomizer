# pylint: disable=C0301

"""E3349_KEEP_6_DOOR_LOBBY_EXIT_TO_PREV_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarNotEqualsConst(KEEP_DOORS_EXIT_TYPE_1, 0, ["EVENT_3349_ret_2"]),
        EnterArea(
            room_id=R452_BOWSERS_KEEP_AREA_06_SAVE_POINT_WCROCO_SHOP,
            face_direction=SOUTHWEST,
            x=16,
            y=80,
            z=0,
            run_entrance_event=True),
        Return(identifier="EVENT_3349_ret_2"),
    ]
)
