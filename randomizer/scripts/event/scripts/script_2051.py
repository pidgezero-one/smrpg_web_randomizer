# pylint: disable=C0301

"""E2051_MONSTRO_SHOP_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
                ASWalkSoutheastPixels(8),
                ASWalkNortheastPixels(2),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
                ASWalkSoutheastPixels(12),
                ASWalkSouthwestPixels(4),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASShadowOff(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
                ASWalkSoutheastPixels(8),
                ASWalkSouthwestPixels(4),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASShadowOff(),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
                ASWalkSoutheastPixels(4),
                ASWalkSouthwestPixels(4),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASShadowOff(),
            ]),
        ApplySolidityModToLevel(
            permanent=True, room_id=R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, mod_id=0
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
