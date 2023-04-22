# pylint: disable=C0301

"""E0671_MARRYMORE_BACK_AREA_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_671_enter_area_3"]),
        EnterArea(
            room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
            face_direction=NORTHEAST,
            x=21,
            y=64,
            z=6,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R064_MARRYMORE_OUTSIDE,
            face_direction=NORTHEAST,
            x=21,
            y=64,
            z=6,
            run_entrance_event=True,
            identifier="EVENT_671_enter_area_3",
        ),
        Return(),
    ]
)
