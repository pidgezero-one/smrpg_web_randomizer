# pylint: disable=C0301

"""E2147_KEEP_ORIGINAL_THRONE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM,
            mod_id=0,
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASWalkNorthwestPixels(8)]),
        ActionQueueSync(target=NPC_3, subscript=[ASWalkSoutheastPixels(8)]),
        ActionQueueSync(target=NPC_4, subscript=[ASWalkSoutheastPixels(8)]),
        ActionQueueSync(target=NPC_5, subscript=[ASWalkNorthwestPixels(8)]),
        ActionQueueSync(target=NPC_6, subscript=[ASWalkSoutheastPixels(8)]),
        ActionQueueAsync(target=NPC_7, subscript=[ASWalkSoutheastPixels(8)]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 12, ["EVENT_2147_fade_in_from_black_async_13"]
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=2, y=66, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=2, y=67, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS),
        SetSyncActionScript(NPC_1, A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2147_fade_in_from_black_async_13"
        ),
        Return(),
    ]
)
