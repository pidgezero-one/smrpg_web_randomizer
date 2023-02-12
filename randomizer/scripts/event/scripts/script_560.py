# E0560_OLD_KEY_ITEM_MANAGER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 189, ["EVENT_560_remove_from_current_level_34"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 83, ["EVENT_560_remove_from_current_level_41"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 84, ["EVENT_560_remove_from_current_level_49"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 301, ["EVENT_560_jmp_if_var_equals_const_57"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_560_jmp_if_bit_clear_69"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 34, ["EVENT_560_remove_from_current_level_95"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            195,
            ["EVENT_560_jmp_if_objects_less_than_xy_steps_apart_102"],
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            41,
            ["EVENT_560_jmp_if_objects_less_than_xy_steps_apart_111"],
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 316, ["EVENT_560_remove_from_current_level_119"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 324, ["EVENT_560_remove_from_current_level_126"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 254, ["EVENT_560_remove_from_current_level_133"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 414, ["EVENT_560_jmp_if_bit_set_140"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            409,
            ["EVENT_560_jmp_if_objects_less_than_xy_steps_apart_152"],
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 107, ["EVENT_560_remove_from_current_level_153"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 438, ["EVENT_560_action_queue_async_161"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 208, ["EVENT_560_jmp_if_bit_clear_236"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 422, ["EVENT_560_store_item_amount_7000_250"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 118, ["EVENT_560_freeze_all_npcs_until_return_273"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 418, ["EVENT_560_set_307"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 483, ["EVENT_560_jmp_if_bit_set_355"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 491, ["EVENT_560_jmp_if_bit_set_355"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 75, ["EVENT_560_set_373"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 272, ["EVENT_560_set_395"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 86, ["EVENT_560_jmp_if_bit_set_28"]),
        Return(),
        JmpIfBitSet(
            ROSE_TOWN_GAZ_ITEM_GRANTED,
            ["EVENT_560_ret_33"],
            identifier="EVENT_560_jmp_if_bit_set_28",
        ),
        SetBit(ROSE_TOWN_GAZ_ITEM_GRANTED),
        SetVarToConst(ITEM_ID, FingerShot),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(identifier="EVENT_560_ret_33"),
        RemoveObjectFromCurrentLevel(
            NPC_3, identifier="EVENT_560_remove_from_current_level_34"
        ),
        RemoveObjectFromSpecificLevel(NPC_3, R189_MARIOS_PIPEHOUSE),
        SetVarToConst(ITEM_ID, DryBonesFlag),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_3, identifier="EVENT_560_remove_from_current_level_41"
        ),
        RemoveObjectFromSpecificLevel(NPC_3, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE),
        RemoveObjectFromSpecificLevel(NPC_12, R084_ROSE_TOWN_OUTSIDE),
        SetVarToConst(ITEM_ID, GreaperFlag),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_12, identifier="EVENT_560_remove_from_current_level_49"
        ),
        RemoveObjectFromSpecificLevel(NPC_3, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE),
        RemoveObjectFromSpecificLevel(NPC_12, R084_ROSE_TOWN_OUTSIDE),
        SetVarToConst(ITEM_ID, GreaperFlag),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        JmpIfVarEqualsConst(
            ACTIVE_NPC,
            20,
            ["EVENT_560_jmp_to_event_60"],
            identifier="EVENT_560_jmp_if_var_equals_const_57",
        ),
        JmpIfBitSet(TEMP_7042_2, ["EVENT_560_set_61"]),
        JmpToEvent(E0032_NON_COIN_CHEST_CONTAINER),
        JmpToEvent(
            E0032_NON_COIN_CHEST_CONTAINER, identifier="EVENT_560_jmp_to_event_60"
        ),
        SetVarToConst(ITEM_ID, CricketJam, identifier="EVENT_560_set_61"),
        SetBit(SEWERS_FLIPPED_CHEST_OPENED),
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        SetVarToConst(ITEM_ID, CricketJam),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        JmpIfBitClear(
            MELODY_BAY_ITEM_1_GRANTED,
            ["EVENT_560_set_bit_72"],
            identifier="EVENT_560_jmp_if_bit_clear_69",
        ),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_560_set_bit_79"]),
        JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_560_set_bit_86"]),
        SetBit(MELODY_BAY_ITEM_1_GRANTED, identifier="EVENT_560_set_bit_72"),
        SetVarToConst(ITEM_ID, AltoCard),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Pause(30, identifier="EVENT_560_pause_77"),
        Return(),
        SetBit(MELODY_BAY_ITEM_2_GRANTED, identifier="EVENT_560_set_bit_79"),
        SetVarToConst(ITEM_ID, TenorCard),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Pause(30, identifier="EVENT_560_pause_84"),
        Return(),
        SetBit(MELODY_BAY_ITEM_3_GRANTED, identifier="EVENT_560_set_bit_86"),
        SetBit(UNKNOWN_7093_0),
        SetVarToConst(ITEM_ID, SopranoCard),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Pause(30, identifier="EVENT_560_pause_92"),
        Return(),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_16, identifier="EVENT_560_remove_from_current_level_95"
        ),
        RemoveObjectFromSpecificLevel(NPC_16, R034_YOSTER_ISLE),
        SetVarToConst(ITEM_ID, BigBooFlag),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO,
            NPC_14,
            3,
            3,
            ["EVENT_560_set_208"],
            identifier="EVENT_560_jmp_if_objects_less_than_xy_steps_apart_102",
        ),
        SetBit(TEMP_7043_5),
        SetBit(PORTRAIT_GAME_COMPLETED),
        SetVarToConst(ITEM_ID, ElderKey),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties(), ASFaceSouth()]),
        Return(),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO,
            NPC_6,
            3,
            3,
            ["EVENT_560_set_222"],
            identifier="EVENT_560_jmp_if_objects_less_than_xy_steps_apart_111",
        ),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromSpecificLevel(
            NPC_5,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
        ),
        SetVarToConst(ITEM_ID, RoomKey),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_7, identifier="EVENT_560_remove_from_current_level_119"
        ),
        RemoveObjectFromSpecificLevel(NPC_7, R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH),
        SetVarToConst(ITEM_ID, ShedKey),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_560_remove_from_current_level_126"
        ),
        RemoveObjectFromSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE),
        SetVarToConst(ITEM_ID, TempleKey),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_3, identifier="EVENT_560_remove_from_current_level_133"
        ),
        RemoveObjectFromSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA),
        SetVarToConst(ITEM_ID, Seed),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        JmpIfBitSet(
            RED_CELLAR_GUARD_ITEM_GRANTED,
            ["EVENT_560_ret_151"],
            identifier="EVENT_560_jmp_if_bit_set_140",
        ),
        SetBit(RED_CELLAR_GUARD_ITEM_GRANTED),
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        SetVarToConst(TEMP_70AE, 16),
        Pause(1),
        Pause(1),
        SetVarToConst(ITEM_ID, CastleKey1),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        JmpToEvent(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(identifier="EVENT_560_ret_151"),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO,
            NPC_6,
            3,
            3,
            ["EVENT_560_store_item_amount_7000_292"],
            identifier="EVENT_560_jmp_if_objects_less_than_xy_steps_apart_152",
        ),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_560_remove_from_current_level_153"
        ),
        RemoveObjectFromSpecificLevel(NPC_0, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
        RemoveObjectFromSpecificLevel(
            NPC_0, R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA
        ),
        SetVarToConst(ITEM_ID, CastleKey2),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASResetProperties(),
            ],
            identifier="EVENT_560_action_queue_async_161",
        ),
        Pause(10),
        Pause(10),
        ActionQueueSync(target=MARIO, subscript=[ASPause(30), ASFaceSoutheast()]),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[ASShiftSoutheastSteps(8), ASDb(bytearray(b"\xfd\xf2"))],
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        SetVarToConst(ITEM_ID, Fertilizer),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        SetVarToConst(ITEM_ID, 0, identifier="EVENT_560_set_172"),
        SetVarToConst(ITEM_ID, AltoCard),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_set_188"]),
        SetVarToConst(ITEM_ID, TenorCard),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_set_198"]),
        SetVarToConst(ITEM_ID, AltoCard),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_560_jmp_if_bit_set_351"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 47, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 483, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 491, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        Return(),
        SetVarToConst(ITEM_ID, TenorCard, identifier="EVENT_560_set_188"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(AltoCard),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_560_jmp_if_bit_set_351"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 47, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 483, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 491, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        Return(),
        SetVarToConst(ITEM_ID, SopranoCard, identifier="EVENT_560_set_198"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(TenorCard),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 74, ["EVENT_560_jmp_if_bit_set_351"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 47, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 483, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 491, ["EVENT_560_remove_one_from_inventory_371"]
        ),
        Return(),
        SetVarToConst(ITEM_ID, ElderKey, identifier="EVENT_560_set_208"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_pause_213"]),
        RunDialog(
            dialog_id=DI2801_NEED_THE_KEY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        Pause(5, identifier="EVENT_560_pause_213"),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=33,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=1,
        ),
        RemoveObjectFromCurrentLevel(NPC_14),
        RemoveObjectFromSpecificLevel(
            NPC_14, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM
        ),
        Pause(5),
        RemoveOneOfItemFromInventory(ElderKey),
        Return(),
        SetVarToConst(ITEM_ID, RoomKey, identifier="EVENT_560_set_222"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_pause_227"]),
        RunDialog(
            dialog_id=DI2801_NEED_THE_KEY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        Pause(5, identifier="EVENT_560_pause_227"),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=32,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromSpecificLevel(
            NPC_6,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
        ),
        Pause(5),
        RemoveOneOfItemFromInventory(RoomKey),
        Return(),
        JmpIfBitClear(
            CHAPEL_ITEMS_ANYWHERE_ENABLED,
            ["EVENT_560_set_237"],
            identifier="EVENT_560_jmp_if_bit_clear_236",
        ),
        SetVarToConst(ITEM_ID, ShedKey, identifier="EVENT_560_set_237"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_pause_242"]),
        RunDialog(
            dialog_id=DI2801_NEED_THE_KEY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        Pause(5, identifier="EVENT_560_pause_242"),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(
            NPC_7, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        Pause(5),
        RemoveOneOfItemFromInventory(ShedKey),
        Return(),
        StoreItemAmountTo7000(
            TempleKey, identifier="EVENT_560_store_item_amount_7000_250"
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            0,
            ["EVENT_560_summon_to_current_level_at_marios_coords_254"],
        ),
        RunDialog(
            dialog_id=DI1235_BELOME_STATUE_KEY_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
        SummonObjectToCurrentLevelAtMariosCoords(
            NPC_12, identifier="EVENT_560_summon_to_current_level_at_marios_coords_254"
        ),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetPriority(3),
                ASSetVRAMPriority(PRIORITY_3),
                ASJumpToHeight(112),
                ASWalkToXYCoords(x=1, y=118),
                ASPause(
                    1, identifier="EVENT_560_action_queue_async_255_SUBSCRIPT_pause_6"
                ),
                ASJmpIfObjectInAir(
                    NPC_12, ["EVENT_560_action_queue_async_255_SUBSCRIPT_pause_6"]
                ),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZUpPixels(8),
                ASSetWalkingSpeed(FAST),
                ASShiftZUpPixels(4),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZUpPixels(2),
            ],
        ),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(50),
                ASResetProperties(),
                ASPause(10),
                ASSetSpriteSequence(index=3, looping=False),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_12),
        Pause(60),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_16),
        StartLoopNTimes(2),
        Pause(1, identifier="EVENT_560_pause_263"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_560_pause_263"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        EndLoop(),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[
                ASJumpToHeight(128),
                ASStartLoopNTimes(4),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        RemoveOneOfItemFromInventory(TempleKey),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            mod_id=0,
        ),
        SetBit(TEMPLE_KEY_USED),
        Return(),
        FreezeAllNPCsUntilReturn(
            identifier="EVENT_560_freeze_all_npcs_until_return_273"
        ),
        StoreItemAmountTo7000(CastleKey1),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_560_play_sound_279"]),
        RunDialog(
            dialog_id=DI3600_WAIT_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        UnfreezeAllNPCs(),
        Return(),
        PlaySound(
            sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_560_play_sound_279"
        ),
        Pause(8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        Pause(8),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_10),
        RemoveObjectFromCurrentLevel(NPC_11),
        RemoveObjectFromSpecificLevel(
            NPC_10, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA
        ),
        RemoveObjectFromSpecificLevel(
            NPC_11, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA
        ),
        RemoveOneOfItemFromInventory(CastleKey1),
        UnfreezeAllNPCs(),
        Return(),
        StoreItemAmountTo7000(
            CastleKey2, identifier="EVENT_560_store_item_amount_7000_292"
        ),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_560_play_sound_296"]),
        RunDialog(
            dialog_id=DI2811_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        PlaySound(
            sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_560_play_sound_296"
        ),
        Pause(8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        Pause(8),
        ApplySolidityModToLevel(
            permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=1
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_7, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
        RemoveOneOfItemFromInventory(CastleKey2),
        Return(),
        SetVarToConst(TEMP_70AE, 23, identifier="EVENT_560_set_307"),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["EVENT_560_run_dialog_314"]),
        StoreItemAmountTo7000(Seed),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_560_remove_one_from_inventory_316"]
        ),
        StoreItemAmountTo7000(Fertilizer),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_560_remove_one_from_inventory_322"]
        ),
        Return(),
        RunDialog(
            dialog_id=DI3103_GARDENER_CUTSCENE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_560_run_dialog_314",
        ),
        Return(),
        RemoveOneOfItemFromInventory(
            Seed, identifier="EVENT_560_remove_one_from_inventory_316"
        ),
        SetBit(GAVE_SEED),
        JmpIfBitSet(
            GAVE_FERTILIZER,
            ["EVENT_560_jmp_if_bit_set_318"],
            identifier="EVENT_560_jmp_if_bit_set_318",
        ),
        StoreItemAmountTo7000(Fertilizer),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_560_remove_one_from_inventory_322"]
        ),
        Return(),
        RemoveOneOfItemFromInventory(
            Fertilizer, identifier="EVENT_560_remove_one_from_inventory_322"
        ),
        SetBit(GAVE_FERTILIZER),
        JmpIfBitSet(GAVE_SEED, ["EVENT_560_freeze_camera_328"]),
        StoreItemAmountTo7000(Seed),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_560_remove_one_from_inventory_316"]
        ),
        Return(),
        FreezeCamera(identifier="EVENT_560_freeze_camera_328"),
        SetBit(GAVE_SEED_AND_FERTILIZER),
        SummonObjectToSpecificLevel(NPC_0, R417_GARDENERS_HOUSE_OUTSIDE),
        SummonObjectToSpecificLevel(NPC_1, R417_GARDENERS_HOUSE_OUTSIDE),
        SummonObjectToSpecificLevel(NPC_0, R418_GARDENERS_HOUSE),
        SummonObjectToSpecificLevel(NPC_1, R418_GARDENERS_HOUSE),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=22, y=0)],
        ),
        PlaySound(sound=SO127_LIGHT_RATTLE, channel=6),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASVisibilityOn(),
            ],
        ),
        Pause(24),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(32),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        PlaySound(sound=SO128_FLOATING_HOVERING, channel=6),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(64),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(40),
        SummonObjectToCurrentLevel(NPC_1),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Pause(8),
        SetAsyncActionScript(MARIO, A0857_PLAYER_DENIES_GARDENER),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
        JmpIfBitSet(
            MELODY_BAY_ITEM_3_GRANTED,
            ["EVENT_560_pause_92"],
            identifier="EVENT_560_jmp_if_bit_set_351",
        ),
        JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_560_pause_84"]),
        JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_560_pause_77"]),
        Return(),
        JmpIfBitSet(
            MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED,
            ["EVENT_560_set_361"],
            identifier="EVENT_560_jmp_if_bit_set_355",
        ),
        SetBit(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED),
        SetVarToConst(ITEM_ID, PickMeUp),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        Return(),
        SetVarToConst(ITEM_ID, RareFrogCoin, identifier="EVENT_560_set_361"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_set_367"]),
        OpenShop(SH00_MUSHROOM_KINGDOM),
        FadeInFromBlack(sync=False),
        Return(),
        SetVarToConst(ITEM_ID, CricketPie, identifier="EVENT_560_set_367"),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_560_set_172"]),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(
            RareFrogCoin, identifier="EVENT_560_remove_one_from_inventory_371"
        ),
        Return(),
        SetVarToConst(ITEM_ID, CricketPie, identifier="EVENT_560_set_373"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_set_380"]),
        SetVarToConst(ITEM_ID, CricketJam),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_play_sound_390"]),
        Return(),
        SetVarToConst(ITEM_ID, FroggieStick, identifier="EVENT_560_set_380"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(CricketPie),
        Return(),
        SetVarToConst(ITEM_ID, FroggieStick),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(CricketJam),
        Return(),
        PlaySound(
            sound=SO094_FROG_COIN, channel=6, identifier="EVENT_560_play_sound_390"
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        AddFrogCoins(PRIMARY_TEMP_7000),
        RemoveOneOfItemFromInventory(CricketJam),
        Return(),
        SetVarToConst(ITEM_ID, BambinoBomb, identifier="EVENT_560_set_395"),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_560_set_399"]),
        RunDialog(
            dialog_id=DI1632_PA_MOLE_NEEDS_BOMB,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        SetVarToConst(TEMP_70AE, 20, identifier="EVENT_560_set_399"),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(1),
        Store02To0248(),
        SetBit(BAMBINO_BOMB_UNKNOWN),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES,
            mod_id=32,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES,
            mod_id=0,
        ),
        Pause(2),
        ClearBit(BAMBINO_BOMB_UNKNOWN),
        Store00To0248(),
        Pause(1),
        JmpIfBitClear(TEMP_7043_5, ["EVENT_560_action_queue_sync_414"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalk1StepSoutheast(),
                ASShiftNortheastSteps(2),
                ASWalk1StepNorthwest(),
                ASFaceSouthwest(),
                ASSetAllSpeeds(NORMAL),
            ],
            identifier="EVENT_560_action_queue_sync_414",
        ),
        SetVarToConst(TEMP_70AE, 20),
        SetSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        SetSyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(16),
                ASFaceSouthwest(),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(72),
                ASPause(20),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkToXYCoords(x=6, y=24),
                ASWalkToXYCoords(x=4, y=20),
                ASShiftSouthwestSteps(2),
                ASDb(bytearray(b"\xfd\xf2")),
                ASVisibilityOff(),
            ],
        ),
        SetBit(MINES_BACK_OPENED),
        RemoveOneOfItemFromInventory(BambinoBomb),
        Return(),
    ]
)
