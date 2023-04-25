# pylint: disable=C0301

"""E0720_OLD_STAR_PIECE_SCRIPT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 205, ["EVENT_720_jmp_if_bit_set_71"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 225, ["EVENT_720_play_sound_336"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 202, ["EVENT_720_set_53"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 212, ["EVENT_720_set_211"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 215, ["EVENT_720_start_battle_229"]),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 200, ["EVENT_720_set_33"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 201, ["EVENT_720_set_41"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 203, ["EVENT_720_set_short_61"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 204, ["EVENT_720_set_short_66"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 206, ["EVENT_720_set_short_150"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 207, ["EVENT_720_set_short_155"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 208, ["EVENT_720_summon_to_level_160"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 209, ["EVENT_720_set_short_172"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 210, ["EVENT_720_set_short_177"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 211, ["EVENT_720_jmp_if_bit_set_182"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 213, ["EVENT_720_set_short_219"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 214, ["EVENT_720_set_short_224"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 216, ["EVENT_720_set_256"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 217, ["EVENT_720_set_bit_264"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 218, ["EVENT_720_set_short_300"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 219, ["EVENT_720_set_short_305"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 220, ["EVENT_720_set_short_310"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 221, ["EVENT_720_set_short_315"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 222, ["EVENT_720_set_short_320"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_325"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 224, ["EVENT_720_set_short_331"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 226, ["EVENT_720_set_short_368"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 227, ["EVENT_720_set_short_383"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 228, ["EVENT_720_set_short_388"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 229, ["EVENT_720_set_short_393"]),
        Return(),
        SetVarToConst(ITEM_ID, Hammer, identifier="EVENT_720_set_33"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        Return(),
        SetVarToConst(ITEM_ID, RareFrogCoin, identifier="EVENT_720_set_41"),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_720_set_613"]),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(ITEM_ID, Wallet, identifier="EVENT_720_set_45"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(ITEM_ID, TrueformPin, identifier="EVENT_720_set_53"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_61"),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_66"),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        JmpIfBitSet(
            MINES_BOSS_1_DEFEATED,
            ["EVENT_720_set_93"],
            identifier="EVENT_720_jmp_if_bit_set_71",
        ),
        SetBit(TEMP_7043_0),
        StartBattleAtBattlefield(164, BF05_MOLEVILLE_MINES),
        JmpIfBitSet(GAME_OVER, ["EVENT_720_reset_and_choose_game_366"]),
        FadeInFromBlack(sync=False),
        SetBit(MINES_BOSS_1_DEFEATED),
        RestoreAllHP(),
        RestoreAllFP(),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASPause(32),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASReturn(),
            ],
        ),
        ResumeActionScript(MEM_70A8),
        Set7000ToCurrentLevel(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 277, ["EVENT_720_jmp_if_7000_not_equals_short_87"]
        ),
        JmpIfBitSet(MINES_HENCHMAN_LEFT_DEFEATED, ["EVENT_720_set_93"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(
                    [
                        "EVENT_720_action_queue_sync_106_SUBSCRIPT_object_memory_set_bit_0"
                    ]
                ),
            ],
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            283,
            ["EVENT_720_jmp_if_7000_not_equals_short_90"],
            identifier="EVENT_720_jmp_if_7000_not_equals_short_87",
        ),
        JmpIfBitSet(MINES_HENCHMAN_RIGHT_DEFEATED, ["EVENT_720_set_93"]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(
                    [
                        "EVENT_720_action_queue_sync_122_SUBSCRIPT_object_memory_set_bit_0"
                    ]
                ),
            ],
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            273,
            ["EVENT_720_set_93"],
            identifier="EVENT_720_jmp_if_7000_not_equals_short_90",
        ),
        JmpIfBitSet(MINES_HENCHMAN_MIDDLE_DEFEATED, ["EVENT_720_set_93"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(["EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_0"]),
            ],
        ),
        SetVarToConst(ITEM_ID, BambinoBomb, identifier="EVENT_720_set_93"),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_720_set_613"]),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_97"),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        MoveScriptToMainThread(),
        SetBit(TEMP_7043_0),
        SetVarToConst(BATTLE_PACK_ID, 141),
        RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_720_action_queue_sync_106_SUBSCRIPT_object_memory_set_bit_0",
                ),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceMario(),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(NORMAL),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASPause(
                    1, identifier="EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_10"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_10"]
                ),
                ASPause(32),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASPause(32),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkSoutheastSteps(3),
                ASWalkSouthwestSteps(3),
                ASWalkSoutheastSteps(2),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ],
        ),
        RunDialog(
            dialog_id=DI1644_EMPTY,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(MINES_HENCHMAN_LEFT_DEFEATED),
        SetBit(TEMP_7043_1),
        JmpIfBitSet(RUN_AWAY, ["EVENT_720_close_dialog_115"]),
        SetVarToConst(ITEM_ID, FlowerTab),
        PlaySound(sound=SO085_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI1645_EMPTY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        CloseDialog(identifier="EVENT_720_close_dialog_115"),
        ClearBit(TEMP_7043_0),
        Return(),
        MoveScriptToMainThread(),
        SetBit(TEMP_7043_0),
        SetVarToConst(BATTLE_PACK_ID, 141),
        RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_720_action_queue_sync_122_SUBSCRIPT_object_memory_set_bit_0",
                ),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceMario(),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(NORMAL),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASPause(
                    1, identifier="EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_10"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_10"]
                ),
                ASPause(32),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASPause(32),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkNorthwestSteps(5),
                ASWalkSouthwestSteps(5),
                ASWalkNorthwestSteps(4),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ],
        ),
        RunDialog(
            dialog_id=DI1644_EMPTY,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(MINES_HENCHMAN_RIGHT_DEFEATED),
        SetBit(TEMP_7043_1),
        JmpIfBitSet(RUN_AWAY, ["EVENT_720_close_dialog_131"]),
        SetVarToConst(ITEM_ID, FlowerTab),
        PlaySound(sound=SO085_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI1645_EMPTY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        CloseDialog(identifier="EVENT_720_close_dialog_131"),
        ClearBit(TEMP_7043_0),
        Return(),
        MoveScriptToMainThread(),
        SetBit(TEMP_7043_0),
        SetVarToConst(BATTLE_PACK_ID, 141),
        RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPause(
                    32, identifier="EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_0"
                ),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceMario(),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(NORMAL),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASPause(
                    1, identifier="EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_10"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_10"]
                ),
                ASPause(32),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkSoutheastSteps(4),
                ASWalkNortheastSteps(3),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ],
        ),
        RunDialog(
            dialog_id=DI1644_EMPTY,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(MINES_HENCHMAN_MIDDLE_DEFEATED),
        SetBit(TEMP_7043_1),
        JmpIfBitSet(RUN_AWAY, ["EVENT_720_close_dialog_147"]),
        SetVarToConst(ITEM_ID, FlowerTab),
        PlaySound(sound=SO085_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI1645_EMPTY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        CloseDialog(identifier="EVENT_720_close_dialog_147"),
        ClearBit(TEMP_7043_0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_150"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_155"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SummonObjectToSpecificLevel(
            NPC_0,
            R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM,
            identifier="EVENT_720_summon_to_level_160",
        ),
        SummonObjectToSpecificLevel(NPC_1, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        SummonObjectToSpecificLevel(NPC_2, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_3, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_4, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_5, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_6, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_172"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_177"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        JmpIfBitSet(
            SHIP_MIDBOSS_COMPLETED,
            ["EVENT_720_fade_out_to_black_async_200"],
            identifier="EVENT_720_jmp_if_bit_set_182",
        ),
        StartBattleAtBattlefield(167, BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RestoreAllHP(),
        RestoreAllFP(),
        SetBit(SHIP_MIDBOSS_COMPLETED),
        EnterArea(
            room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
            face_direction=NORTHEAST,
            x=3,
            y=89,
            z=8,
            run_entrance_event=True,
        ),
        ClearBit(DIRECTIONAL_7049_0),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Pause(20),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        FadeOutToBlack(sync=False, identifier="EVENT_720_fade_out_to_black_async_200"),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        EnterArea(
            room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
            face_direction=SOUTH,
            x=2,
            y=92,
            z=8,
            run_entrance_event=True,
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Return(),
        Return(),
        SetVarToConst(ITEM_ID, SafetyBadge, identifier="EVENT_720_set_211"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_219"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_224"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        StartBattleAtBattlefield(
            169, BF42_BELOME_TEMPLE, identifier="EVENT_720_start_battle_229"
        ),
        SetBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RemoveObjectFromCurrentLevel(NPC_1),
        RestoreAllHP(),
        RestoreAllFP(),
        FadeInFromBlack(sync=False),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_0),
        StartLoopNTimes(2),
        Pause(1, identifier="EVENT_720_pause_242"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_720_pause_242"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        EndLoop(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        SummonObjectToSpecificLevel(NPC_1, R324_MONSTRO_TOWN_OUTSIDE),
        SummonObjectToSpecificLevel(NPC_4, R324_MONSTRO_TOWN_OUTSIDE),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        SetBit(TEMPLE_BOSS_DEFEATED),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(ITEM_ID, JinxBelt, identifier="EVENT_720_set_256"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetBit(UNUSED_7093_5, identifier="EVENT_720_set_bit_264"),
        PlayMusicAtDefaultVolume(M51_MONSTRO_TOWN),
        JmpIfBitSet(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, ["EVENT_720_set_bit_275"]),
        CopyVarToVar(from_var=MONSTRO_THWOMP_COUNTER, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_720_action_queue_async_270"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASLoadMemory(PRIMARY_TEMP_7000),
                ASWalkSouthwestSteps(2),
                ASEndLoop(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetSpriteSequence(index=2, is_sequence=True, looping=True)],
            identifier="EVENT_720_action_queue_async_270",
        ),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_720_enable_controls_until_return_281"]),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_720_set_292"]),
        Return(),
        SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, identifier="EVENT_720_set_bit_275"),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=11, y=62, z=8, direction=EAST),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        JmpIfVarEqualsConst(
            FLAG_COLLECTION_7044, 7, ["EVENT_720_enable_controls_until_return_281"]
        ),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_720_set_292"]),
        Return(),
        EnableControlsUntilReturn(
            [], identifier="EVENT_720_enable_controls_until_return_281"
        ),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShadowOff(),
                ASResetProperties(),
                ASFaceSouth(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_720_action_queue_async_285_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_720_action_queue_async_285_SUBSCRIPT_pause_1"]
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShadowOff(),
                ASJumpToHeight(165),
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_720_action_queue_async_285_SUBSCRIPT_pause_10"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_720_action_queue_async_285_SUBSCRIPT_pause_10"]
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_7),
        Jmp(["EVENT_720_set_292"]),
        Return(),
        SetVarToConst(ITEM_ID, QuartzCharm, identifier="EVENT_720_set_292"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_300"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_305"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_310"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_315"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_320"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_325"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0, identifier="EVENT_720_set_short_327"),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        ExitToWorldMap(area=OW50_BARREL_VOLCANO),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_331"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlaySound(
            sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_720_play_sound_336"
        ),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASShiftNorthSteps(2)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x03\x80\xff")),
                ASPause(8),
                ASBPL262728(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        Set70107015ToObjectXYZ(MEM_70A8),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        ClearBit(MIMIC_3_CLEARED),
        PlaySound(sound=SO014_FLOWER, channel=6),
        CreatePacketAt7010(
            packet=P004_MIMIC_POOF_ON_DEFEAT, destinations=["EVENT_720_pause_348"]
        ),
        Pause(32, identifier="EVENT_720_pause_348"),
        StopEmbeddedActionScript(NPC_5),
        StartBattleAtBattlefield(158, BF21_KERO_SEWERS),
        JmpIfBitSet(GAME_OVER, ["EVENT_720_reset_and_choose_game_366"]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASShiftSouthSteps(2), ASSetWalkingSpeed(NORMAL)],
        ),
        FadeInFromBlack(sync=False),
        SetBit(MIMIC_3_CLEARED),
        SetBit(UNKNOWN_MIMIC_BIT),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%@\x00\x80\xff")),
                ASPause(8),
                ASBPL262728(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOff(),
            ],
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM
        ),
        StopEmbeddedActionScript(NPC_5),
        SetAsyncActionScript(NPC_5, A0015_DO_NOTHING),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        ResetAndChooseGame(identifier="EVENT_720_reset_and_choose_game_366"),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_368"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 255),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_383"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_388"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(
            OLD_STAR_PIECE_GRANTER, 255, identifier="EVENT_720_set_short_393"
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_GRANTER, 255, ["EVENT_720_jmp_if_bit_set_398"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        JmpIfBitSet(
            STAR_PIECE_MENU_UNLOCKED,
            ["EVENT_720_jmp_if_var_equals_const_400"],
            identifier="EVENT_720_jmp_if_bit_set_398",
        ),
        SetBit(STAR_PIECE_MENU_UNLOCKED),
        JmpIfVarEqualsConst(
            EXP_STAR_70D5,
            6,
            ["EVENT_720_jmp_if_bit_clear_478"],
            identifier="EVENT_720_jmp_if_var_equals_const_400",
        ),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 5, ["EVENT_720_inc_463"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 4, ["EVENT_720_inc_452"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 3, ["EVENT_720_inc_441"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 2, ["EVENT_720_inc_430"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 1, ["EVENT_720_inc_419"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 0, ["EVENT_720_inc_408"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_408"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(1),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_419"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(2),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_430"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(3),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_441"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(4),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_452"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(5),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        Inc(EXP_STAR_70D5, identifier="EVENT_720_inc_463"),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(6),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        JmpIfBitSet(UNUSED_7089_5, ["EVENT_720_jmp_if_bit_clear_499"]),
        JmpIfBitSet(UNKNOWN_STAR_PIECE, ["EVENT_720_fade_in_from_black_async_510"]),
        SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BOWSERS_KEEP),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        JmpIfBitClear(
            UNKNOWN_STAR_PIECE,
            ["EVENT_720_ret_492"],
            identifier="EVENT_720_jmp_if_bit_clear_478",
        ),
        Inc(EXP_STAR_70D5),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        RunStarPieceSequence(7),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01")),
        PauseScriptUntilEffectDone(),
        JmpIfBitSet(UNUSED_7089_5, ["EVENT_720_set_bit_493"]),
        SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BOWSERS_KEEP),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(identifier="EVENT_720_ret_492"),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, identifier="EVENT_720_set_bit_493"),
        SetBit(MAP_GATE),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        JmpIfBitClear(
            UNKNOWN_STAR_PIECE,
            ["EVENT_720_set_bit_504"],
            identifier="EVENT_720_jmp_if_bit_clear_499",
        ),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, identifier="EVENT_720_set_bit_504"),
        SetBit(MAP_GATE),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_720_fade_in_from_black_async_510"
        ),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BOWSERS_KEEP),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
        FadeInFromBlack(sync=False),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 223, ["EVENT_720_set_short_327"]),
        Jmp(["EVENT_720_jmp_if_var_equals_const_520"]),
        Return(),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID,
            202,
            ["EVENT_720_play_music_default_volume_561"],
            identifier="EVENT_720_jmp_if_var_equals_const_520",
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 204, ["EVENT_720_play_music_default_volume_565"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 205, ["EVENT_720_play_music_default_volume_561"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 206, ["EVENT_720_play_music_default_volume_561"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 207, ["EVENT_720_play_music_default_volume_569"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 208, ["EVENT_720_play_music_default_volume_549"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 209, ["EVENT_720_play_music_default_volume_577"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 210, ["EVENT_720_play_music_default_volume_581"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 211, ["EVENT_720_play_music_default_volume_585"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 212, ["EVENT_720_play_music_default_volume_585"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 213, ["EVENT_720_play_music_default_volume_585"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 214, ["EVENT_720_play_music_default_volume_589"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 215, ["EVENT_720_play_music_default_volume_561"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 216, ["EVENT_720_play_music_default_volume_605"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 217, ["EVENT_720_play_music_default_volume_605"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 218, ["EVENT_720_play_music_default_volume_553"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 219, ["EVENT_720_play_music_default_volume_593"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 220, ["EVENT_720_play_music_default_volume_593"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 221, ["EVENT_720_play_music_default_volume_597"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 222, ["EVENT_720_play_music_default_volume_601"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 224, ["EVENT_720_play_music_default_volume_557"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 225, ["EVENT_720_play_music_default_volume_553"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 226, ["EVENT_720_play_music_default_volume_605"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 227, ["EVENT_720_play_music_default_volume_609"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 228, ["EVENT_720_play_music_default_volume_609"]
        ),
        JmpIfVarEqualsConst(
            OLD_STAR_PIECE_ID, 229, ["EVENT_720_play_music_default_volume_609"]
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M13_ROAD_IS_FULL_OF_DANGERS,
            identifier="EVENT_720_play_music_default_volume_549",
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
            identifier="EVENT_720_play_music_default_volume_553",
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M02_MUSHROOM_KINGDOM, identifier="EVENT_720_play_music_default_volume_557"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M27_DUNGEON_IS_FULL_OF_MONSTERS,
            identifier="EVENT_720_play_music_default_volume_561",
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M26_FOREST_MAZE, identifier="EVENT_720_play_music_default_volume_565"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M31_BOOSTERS_TOWER, identifier="EVENT_720_play_music_default_volume_569"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(M13_ROAD_IS_FULL_OF_DANGERS),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M39_MARRYMORE, identifier="EVENT_720_play_music_default_volume_577"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M34_STAR_HILL, identifier="EVENT_720_play_music_default_volume_581"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M41_SUNKEN_SHIP, identifier="EVENT_720_play_music_default_volume_585"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M05_SEASIDE_TOWN, identifier="EVENT_720_play_music_default_volume_589"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M61_VALENTINA, identifier="EVENT_720_play_music_default_volume_593"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M50_NIMBUS_LAND, identifier="EVENT_720_play_music_default_volume_597"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M62_BARREL_VOLCANO, identifier="EVENT_720_play_music_default_volume_601"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M51_MONSTRO_TOWN, identifier="EVENT_720_play_music_default_volume_605"
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        PlayMusicAtDefaultVolume(
            M66_BOWSERS_CASTLE_2ND_TIME,
            identifier="EVENT_720_play_music_default_volume_609",
        ),
        SetVarToConst(OLD_STAR_PIECE_ID, 0),
        SetVarToConst(OLD_STAR_PIECE_GRANTER, 0),
        Return(),
        SetVarToConst(ITEM_ID, 0, identifier="EVENT_720_set_613"),
        SetVarToConst(ITEM_ID, AltoCard),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_720_set_626"]),
        SetVarToConst(ITEM_ID, TenorCard),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_720_set_633"]),
        SetVarToConst(ITEM_ID, AltoCard),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 201, ["EVENT_720_set_45"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 205, ["EVENT_720_set_short_97"]),
        Return(),
        SetVarToConst(ITEM_ID, TenorCard, identifier="EVENT_720_set_626"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(AltoCard),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 201, ["EVENT_720_set_45"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 205, ["EVENT_720_set_short_97"]),
        Return(),
        SetVarToConst(ITEM_ID, SopranoCard, identifier="EVENT_720_set_633"),
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
        RemoveOneOfItemFromInventory(TenorCard),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 201, ["EVENT_720_set_45"]),
        JmpIfVarEqualsConst(OLD_STAR_PIECE_ID, 205, ["EVENT_720_set_short_97"]),
        Return(),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["50990"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["10715"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["35983"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["61237"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["20941"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["46188"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["5878"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["31111"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["56330"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["15999"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["41211"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["866"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["26069"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["51248"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["10882"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["36059"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["61222"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["20835"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["45991"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["5590"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["30732"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["55860"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["15438"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["40567"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["123"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["25250"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["50323"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["9866"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["34952"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["60024"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["19546"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["44611"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["4119"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["29170"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["54207"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["13694"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["39739"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["63733"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["23213"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["48215"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["32662"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["57643"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["17074"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["42048"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["1465"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["26425"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["51371"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["10767"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["35706"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["60631"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["20006"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["44924"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["4285"]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(MARIO, MARIO, 0, 0, ["54079"]),
        StopSound(),
        Return(),
    ]
)
