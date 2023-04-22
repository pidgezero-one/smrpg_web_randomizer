# pylint: disable=C0301

"""E0916_CHEST_YELLOW_BOMB_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P190_YELLOW_BOMB_CHEST, destinations=["EVENT_916_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_916_final_ret"),
    ]
)
