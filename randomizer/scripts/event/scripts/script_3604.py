# pylint: disable=C0301

"""E3604_PIPE_VAULT_TRIPLE_CHEST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_3604_ret_6"]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[ASTransferXYZFPixels(x=254, y=250, z=0, direction=EAST)]),
        Return(identifier="EVENT_3604_ret_6"),
    ]
)
