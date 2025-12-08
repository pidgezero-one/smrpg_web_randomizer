# pylint: disable=C0301

"""E3165_ACTIVE_MINECART_MARIO_COLLISION_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_3, ["EVENT_3165_ret_3"]),
        RunBackgroundEvent(
            event_id=E3166_ACTIVE_MINECART_MARIO_COLLISION_CHECK_PROPERTIES,
            return_on_level_exit=True),
        SetBit(TEMP_7044_3),
        Return(identifier="EVENT_3165_ret_3"),
    ]
)
