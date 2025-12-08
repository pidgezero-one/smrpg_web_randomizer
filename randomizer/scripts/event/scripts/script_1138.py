# pylint: disable=C0301

"""E1138_SEASIDE_OCCUPIED_WPN_ARM_SHOP_OCCUPANT_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSequenceLoopingOff(),
                ASPause(50),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=15, y=65, height=0),
                ASFaceSoutheast(),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPause(20),
                ASFaceSouthwest(),
                ASPause(40),
                ASFaceSoutheast(),
                ASPause(20),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=13, y=69, height=0),
                ASFaceMario(),
                ASSetSequenceSpeed(FAST),
            ]),
        Pause(25),
        RunDialog(
            dialog_id=DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(target=NPC_0, subscript=[ASFaceSoutheast()]),
        Return(),
    ]
)
