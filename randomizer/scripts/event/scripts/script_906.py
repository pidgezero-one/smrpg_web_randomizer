# pylint: disable=C0301

"""E0906_CHEST_FROG_DRINK_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P157_FROG_DRINK_CHEST, destinations=["EVENT_906_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_906_final_ret"),
    ]
)
