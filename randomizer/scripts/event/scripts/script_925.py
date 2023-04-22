# pylint: disable=C0301

"""E0925_CHEST_FAN_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(packet=P217_FAN_CHEST, destinations=["EVENT_925_final_ret"]),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_925_final_ret"),
    ]
)
