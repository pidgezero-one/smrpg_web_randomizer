# pylint: disable=C0301

"""E0921_CHEST_FRYING_PAN_PACKET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P205_FRYING_PAN_CHEST, destinations=["EVENT_921_final_ret"]
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        Return(identifier="EVENT_921_final_ret"),
    ]
)
