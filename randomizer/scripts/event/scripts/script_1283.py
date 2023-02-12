# E1283_TOWER_BALCONY_LOADER_BEFORE_MARRYMORE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=7, y=14, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASVisibilityOff()]),
        ActionQueueSync(target=NPC_1, subscript=[ASVisibilityOff()]),
        ActionQueueSync(target=NPC_2, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_3, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        JmpToEvent(E1927_TOWER_BALCONY_JUMP_OFF),
    ]
)
