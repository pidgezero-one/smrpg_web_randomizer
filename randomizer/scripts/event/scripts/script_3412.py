# pylint: disable=C0301

"""E3412_MINES_SHYGUY_ITEM_CREATE_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CreatePacketAt7010WithEvent(
            packet=P111_FROG_COIN_STATIC,
            event_id=E3199_SHYGUY_CART_PRIZE_GRANT,
            destinations=["EVENT_3413_r"],
        ),
        Jmp(["EVENT_3413_action_queue_sync_15"]),
    ]
)
