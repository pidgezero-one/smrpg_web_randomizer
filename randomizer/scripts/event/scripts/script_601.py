# pylint: disable=C0301

"""E0601_MARRYMORE_BACK_DOOR_ENTER_CHAPEL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_601_ret_2"]),
        EnterArea(
            room_id=R156_MARRYMORE_CHAPEL_KITCHEN_NO_SPRITESEXITS_UNUSED,
            face_direction=SOUTHWEST,
            x=5,
            y=89,
            z=2,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_601_ret_2"),
    ]
)
