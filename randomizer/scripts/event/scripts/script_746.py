# pylint: disable=C0301

"""E0746_MUSHROOM_KINGDOM_INN_2F_DOWNWARD_STAIRS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_746_enter_area_6"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_746_enter_area_8"]),
        EnterArea(
            room_id=R191_MUSHROOM_KINGDOM_OUTSIDE,
            face_direction=SOUTHWEST,
            x=14,
            y=99,
            z=4,
            run_entrance_event=True,
            identifier="EVENT_746_enter_area_6"),
        Return(),
        EnterArea(
            room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            face_direction=SOUTHWEST,
            x=14,
            y=99,
            z=4,
            run_entrance_event=True,
            identifier="EVENT_746_enter_area_8"),
        Return(),
    ]
)
