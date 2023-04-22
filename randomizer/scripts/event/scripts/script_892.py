# pylint: disable=C0301

"""E0892_CHEST_EGG_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(packet=P117_EGG_CHEST, destinations=["EVENT_892_final_ret"]),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_892_final_ret"),
    ]
)
