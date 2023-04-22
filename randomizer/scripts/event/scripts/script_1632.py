# pylint: disable=C0301

"""E1632_MOLEVILLE_MINECART_FREEPLAY_ENDING_LANDING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASBounceToXYWithHeight(x=24, y=44, height=8),
                ASFaceMario(),
            ],
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest7D()]),
        RunDialog(
            dialog_id=DI1136_TOUCH_MINECART,
            above_object=NPC_3,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(SLOW),
                ASBounceToXYWithHeight(x=25, y=40, height=8),
                ASFaceSouthwest(),
            ],
        ),
        Return(),
    ]
)
