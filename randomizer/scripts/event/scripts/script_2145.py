# pylint: disable=C0301

"""E2145_KEEP_DONUT_BRIDGE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=32),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=35),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=36),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            mod_id=0),
        RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
        ActionQueueSync(target=NPC_0, subscript=[ASFaceNortheast(), ASPause(1)]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestPixels(14),
                ASWalkSoutheastPixels(8),
            ]),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestPixels(14),
                ASWalkSoutheastPixels(8),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestPixels(14),
                ASWalkSoutheastPixels(8),
            ]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 16, ["EVENT_2145_fade_in_from_black_async_14"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=16, y=42, z=10, direction=EAST),
                ASFaceSouthwest(),
                ASPause(1),
            ]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2145_fade_in_from_black_async_14"
        ),
        Return(),
    ]
)
