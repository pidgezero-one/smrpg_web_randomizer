# pylint: disable=C0301

"""E2124_CHOOSE_MARRYMORE_SANCTUARY_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_2124_enter_area_7"]),
        JmpIfBitSet(CHAPEL_ITEM_RETRIEVAL_STARTED, ["EVENT_2124_enter_area_7_"]),
        JmpToEvent(E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE),
        EnterArea(
            room_id=R065_MARRYMORE_CHAPEL_SANCTUARY,
            face_direction=NORTHEAST,
            x=9,
            y=98,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_2124_enter_area_7",
        ),
        Return(),
        EnterArea(
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            face_direction=NORTHEAST,
            x=9,
            y=98,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_2124_enter_area_7_",
        ),
        Return(),
    ]
)
