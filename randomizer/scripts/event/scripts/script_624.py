# pylint: disable=C0301

"""E0624_MARRYMORE_INN_LOBBY_STAIRS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7044_5),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_256_ret_0"]),
        EnterArea(
            room_id=R006_MARRYMORE_INN_2F,
            face_direction=NORTHEAST,
            x=15,
            y=52,
            z=1,
            z_add_half_unit=True,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
