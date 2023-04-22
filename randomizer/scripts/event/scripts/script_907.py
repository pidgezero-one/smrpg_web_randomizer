# pylint: disable=C0301

"""E0907_CHEST_RED_M_DRINK_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P160_RED_MUSIC_DRINK_CHEST, destinations=["EVENT_907_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_907_final_ret"),
    ]
)
