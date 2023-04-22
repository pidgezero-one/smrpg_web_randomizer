# pylint: disable=C0301

"""E0883_CHEST_ITEM_BAG_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P005_BRIEF_POOF_BAG, destinations=["EVENT_883_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_883_final_ret"),
    ]
)
