# pylint: disable=C0301

"""E3387_SHIP_CANNONBALL_PUZZLE_SPAWN_PRIZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CreatePacketAt7010WithEvent(
            packet=P037_ITEM_BAG_FALL,
            event_id=E3291_SHIP_COLLECT_CANNONBALL_PRIZE,
            destinations=["EVENT_3387_ret"]),
        Return(identifier="EVENT_3387_ret"),
    ]
)
