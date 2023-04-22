# pylint: disable=C0301

"""E0913_CHEST_GREEN_BOMB_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P181_GREEN_BOMB_CHEST, destinations=["EVENT_913_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_913_final_ret"),
    ]
)
