# pylint: disable=C0301

"""E0903_CHEST_D_DRINK_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P148_D_DRINK_CHEST, destinations=["EVENT_903_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_903_final_ret"),
    ]
)
