# pylint: disable=C0301

"""E3854_WORLD_MAP_BOOSTER_PASS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 26, ["EVENT_3854_enter_area_3"]),
        EnterArea(
            room_id=R100_BOOSTER_PASS_AREA_01,
            face_direction=NORTHEAST,
            x=3,
            y=41,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R101_BOOSTER_PASS_AREA_02,
            face_direction=SOUTHWEST,
            x=13,
            y=95,
            z=6,
            run_entrance_event=True,
            identifier="EVENT_3854_enter_area_3",
        ),
        Return(),
    ]
)
