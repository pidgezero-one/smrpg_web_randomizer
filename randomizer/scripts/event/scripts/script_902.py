# pylint: disable=C0301

"""E0902_CHEST_P_DRINK_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P147_P_DRINK_CHEST, destinations=["EVENT_902_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_902_final_ret"),
    ]
)
