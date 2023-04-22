# pylint: disable=C0301

"""E0911_CHEST_GREEN_CANDY_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P175_GREEN_CANDY_CHEST, destinations=["EVENT_911_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_911_final_ret"),
    ]
)
