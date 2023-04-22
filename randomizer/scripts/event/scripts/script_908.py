# pylint: disable=C0301

"""E0908_CHEST_R_DRINK_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P165_R_DRINK_CHEST, destinations=["EVENT_908_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_908_final_ret"),
    ]
)
