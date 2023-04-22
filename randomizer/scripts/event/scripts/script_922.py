# pylint: disable=C0301

"""E0922_CHEST_HAMMER_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P208_HAMMER_CHEST, destinations=["EVENT_922_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_922_final_ret"),
    ]
)
