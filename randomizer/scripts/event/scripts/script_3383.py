# pylint: disable=C0301

"""E3383_SHIP_TRAMPOLINE_PRIZE_PACKET_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CreatePacketAt7010WithEvent(
            packet=P035_FLOWER_FALL,
            event_id=E3289_SHIP_COLLECT_TRAMPOLINE_PRIZE,
            destinations=["EVENT_3210_pause_69"]),
        Jmp(["EVENT_3210_action_queue_async_71"]),
    ]
)
