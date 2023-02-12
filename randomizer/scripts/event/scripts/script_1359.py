# E1359_CURTAIN_GAME_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_7026, 0),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASShiftSouthPixels(22),
                ASShiftEastPixels(7),
                ASSetPriority(2),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(target=NPC_6, subscript=[ASShadowOff()]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShiftNortheastPixels(5),
                ASShiftNorthwestPixels(4),
                ASFaceSoutheast(),
                ASSetPriority(3),
                ASShadowOff(),
            ],
        ),
        ActionQueueAsync(
            target=LAYER_1, subscript=[ASShiftEastPixels(8), ASShiftNorthPixels(8)]
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=2,
        ),
        JmpIfBitSet(FAST_TRAVEL_ENABLED, ["EVENT_1359_jmp_if_bit_set_6"]),
        JmpIfBitClear(TOWER_BOSS_2_DEFEATED, ["EVENT_1359_jmp_if_bit_set_6"]),
        SummonObjectToCurrentLevel(NPC_8),
        SummonObjectToCurrentLevel(NPC_9),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASShiftWestPixels(8), ASShiftSouthPixels(8)]
        ),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASShiftWestPixels(8), ASShiftSouthPixels(8)]
        ),
        JmpIfBitSet(
            CURTAIN_MINIGAME_COMPLETED,
            ["EVENT_1359_apply_tile_mod_10"],
            identifier="EVENT_1359_jmp_if_bit_set_6",
        ),
        JmpIfBitSet(TOWER_BOSS_1_DEFEATED, ["EVENT_1359_apply_solidity_mod_20"]),
        RunEventAsSubroutine(
            E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=35,
            identifier="EVENT_1359_apply_tile_mod_10",
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47,
        ),
        ActionQueueAsync(
            target=NPC_5, subscript=[ASTransferToXYZF(x=3, y=21, z=0, direction=EAST)]
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=1,
        ),
        JmpIfBitClear(UNKNOWN_7054_4, ["EVENT_1359_fade_in_from_black_async_18"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33,
        ),
        RunEventAsSubroutine(
            E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_1359_fade_in_from_black_async_18"
        ),
        Return(),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=2,
            identifier="EVENT_1359_apply_solidity_mod_20",
        ),
        RunEventAsSubroutine(
            E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
