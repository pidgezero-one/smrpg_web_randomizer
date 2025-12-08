# pylint: disable=C0301

"""E3414_ROSE_WAY_MAIN_ROOM_2ND_FREESTANDING_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CreatePacketAt7010WithEvent(
            packet=P086_FLOWER_STATIC,
            event_id=E0240_FREESTANDING_2_GRANT,
            destinations=["EVENT_3414_ret"]),
        Return(identifier="EVENT_3414_ret"),
    ]
)
