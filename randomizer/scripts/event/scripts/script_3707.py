# pylint: disable=C0301

"""E3707_NIMBUS_CASTLE_WEST_STAIRCASE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_704C_0, ["EVENT_3707_action_queue_async_6"]),
        SetBit(GUEST_DROPPED_OFF),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[ASVisibilityOff()],
            identifier="EVENT_3707_action_queue_async_6"),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            mod_id=1),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
