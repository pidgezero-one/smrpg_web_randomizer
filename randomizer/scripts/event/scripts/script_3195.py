# pylint: disable=C0301

"""E3195_PARKED_MINECART_MARIO_COLLISION_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_3, ["EVENT_3195_ret_3"]),
        RunBackgroundEvent(
            event_id=E3196_PARKED_MINECART_MARIO_COLLISION_CHECK_PROPERTIES,
            return_on_level_exit=True,
        ),
        SetBit(TEMP_7044_3),
        Return(identifier="EVENT_3195_ret_3"),
    ]
)
