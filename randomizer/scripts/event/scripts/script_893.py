# pylint: disable=C0301

"""E0893_CHEST_COOKIE_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P120_COOKIE_CHEST, destinations=["EVENT_893_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_893_final_ret"),
    ]
)
