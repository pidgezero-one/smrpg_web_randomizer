# pylint: disable=C0301

"""E1139_SEASIDE_OCCUPIED_WPN_ARM_SHOP_OCCUPANT_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSequenceLoopingOff(),
                ASPause(50),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=14, y=68, height=0),
                ASFaceSoutheast(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(20),
                ASFaceNortheast(),
                ASPause(40),
                ASFaceSoutheast(),
                ASPause(20),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=16, y=64, height=0),
                ASFaceMario(),
                ASSetSequenceSpeed(FAST),
            ],
        ),
        Pause(25),
        RunDialog(
            dialog_id=DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(target=NPC_1, subscript=[ASFaceSoutheast()]),
        Return(),
    ]
)
