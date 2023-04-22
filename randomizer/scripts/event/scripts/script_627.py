# pylint: disable=C0301

"""E0627_MARRYMORE_SANCTUARY_EXIT_TO_ANTECHAMBER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["EVENT_627_enter_area_1"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_627_ret_2"]),
        EnterArea(
            room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            face_direction=SOUTHWEST,
            x=20,
            y=16,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_627_enter_area_1",
        ),
        Return(identifier="EVENT_627_ret_2"),
    ]
)
