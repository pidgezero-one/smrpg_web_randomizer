# pylint: disable=C0301

"""E2572_BOOSTER_PASS_EXIT_FROM_ROOM_1_TO_ROOM_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING, ["EVENT_2572_ret_2"]),
        EnterArea(
            room_id=R101_BOOSTER_PASS_AREA_02,
            face_direction=NORTHEAST,
            x=1,
            y=121,
            z=0,
            run_entrance_event=True),
        Return(identifier="EVENT_2572_ret_2"),
    ]
)
