# pylint: disable=C0301

"""E0885_CHEST_STAR_PIECE_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P081_STAR_PIECE_CHEST, destinations=["EVENT_885_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_885_final_ret"),
    ]
)
