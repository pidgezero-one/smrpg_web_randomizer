# E0404_MUSHROOM_KINGDOM_OCCUPIED_SHOP_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_0),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=29, direction=NORTHEAST)],
        ),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=16, y=16, z=4, direction=EAST)]
        ),
        SetSyncActionScript(NPC_0, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
    ]
)
