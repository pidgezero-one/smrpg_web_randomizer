# E0454_GOOMBA_THUMPIN_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_7028, 0),
        ActionQueueSync(target=NPC_1, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_2, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_3, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_4, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(target=NPC_8, subscript=[ASShadowOff(), ASSetPriority(3)]),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASShadowOff(),
                ASSetPriority(3),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_11,
            subscript=[
                ASShadowOff(),
                ASSetPriority(3),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASShadowOff(),
                ASSetPriority(3),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASShadowOff(),
                ASSetPriority(3),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_14,
            subscript=[
                ASTransferXYZFPixels(x=2, y=6, z=0, direction=EAST),
                ASSetPriority(3),
                ASShadowOff(),
            ],
        ),
        RememberLastObject(),
        PaletteSet(palette_set=110, row=1),
        Pause(2),
        Return(),
    ]
)
