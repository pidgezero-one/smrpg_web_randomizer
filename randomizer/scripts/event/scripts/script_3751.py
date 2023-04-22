# pylint: disable=C0301

"""E3751_NIMBUS_LAND_HOT_SPRINGS_LOBBY_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(HOT_SPRING_GUARD_POSITION, ["EVENT_3751_ret_1"]),
        EnterArea(
            room_id=R447_NIMBUS_LAND_HOT_SPRINGS,
            face_direction=NORTHEAST,
            x=11,
            y=113,
            z=5,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_3751_ret_1"),
    ]
)
