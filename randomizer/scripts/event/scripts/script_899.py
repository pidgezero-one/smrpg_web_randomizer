# pylint: disable=C0301

"""E0899_CHEST_YELLOW_SYRUP_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P138_YELLOW_SYRUP_CHEST, destinations=["EVENT_899_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_899_final_ret"),
    ]
)
