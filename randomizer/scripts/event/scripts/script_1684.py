# pylint: disable=C0301

"""E1684_TEMPLE_ELEVATOR_LOWER_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMPLE_BOSS_ACCESS_FORTUNE, ["EVENT_1684_enter_area_3"]),
        EnterArea(
            room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            face_direction=SOUTHEAST,
            x=1,
            y=116,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM,
            face_direction=SOUTHEAST,
            x=26,
            y=11,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_1684_enter_area_3"),
        Return(),
    ]
)
