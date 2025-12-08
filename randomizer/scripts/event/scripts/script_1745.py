# pylint: disable=C0301

"""E1745_WHIRLPOOL_SHOGUN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASPlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
                ASVisibilityOn(),
                ASSetAllSpeeds(FAST),
                ASShiftZUpPixels(8),
                ASShiftZDownPixels(8),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSet700CToObjectCoord(
                    target_npc=DUMMY_0X07, coord=COORD_X, pixel=True
                ),
                ASCompare700CToVar(X_COORD_1),
                ASJmpIfComparisonResultIsLesser(
                    ["EVENT_1745_action_queue_async_3_SUBSCRIPT_play_sound_10"]
                ),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASPlaySound(
                    sound=SO030_SURPRISED_MONSTER,
                    channel=4,
                    identifier="EVENT_1745_action_queue_async_3_SUBSCRIPT_play_sound_10"),
                ASJumpToHeight(108),
                ASPause(32),
            ]),
        SetVarToConst(BATTLE_PACK_ID, 206),
        StartBattleWithPackAt700E(),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1745_action_queue_async_31"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1745_reset_and_choose_game_29"]),
        RemoveObjectAt70A8FromCurrentLevel(),
        Pause(1),
        DisableObjectTrigger(MEM_70A8),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        Pause(1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASTurnClockwise45DegreesNTimes(4),
                ASWalkFDirectionPixels(10),
                ASTurnClockwise45DegreesNTimes(4),
                ASSetAllSpeeds(NORMAL),
            ]),
        SetBit(TEMP_7043_2),
        FadeInFromBlack(sync=False),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        StartLoopNTimes(2),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    cant_jump_through=True, bit_4=True, cant_walk_through=True
                )
            ]),
        Inc(ACTIVE_NPC),
        EndLoop(),
        Pause(1),
        SetVarToConst(TIMER_701C, 90),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1789_WHIRLPOOL_SHOGUN_SUBROUTINE, timer_var=TIMER_701C
        ),
        SetBit(TEMP_7043_2),
        SetBit(TEMP_7043_3),
        UnfreezeAllNPCs(),
        Return(),
        ResetAndChooseGame(identifier="EVENT_1745_reset_and_choose_game_29"),
        Return(),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASDb(bytearray(b"\xc8\x07")),
                ASSetVarToConst(Z_COORD_2, 0),
                ASDb(bytearray(b"\x99")),
                ASSetAllSpeeds(NORMAL),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASSetSolidityBits(cant_walk_through=True),
            ],
            identifier="EVENT_1745_action_queue_async_31"),
        PauseActionScript(MARIO),
        ResetCoords(MARIO),
        Pause(1),
        Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Y, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(FASTEST),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
                ASCompare700CToVar(Y_COORD_1),
                ASJmpIfComparisonResultIsGreaterOrEqual(
                    ["EVENT_1745_action_queue_async_37_SUBSCRIPT_shift_south_pixels_7"]
                ),
                ASWalkNorthPixels(14),
                ASJmp(["EVENT_1745_action_queue_async_37_SUBSCRIPT_face_north_8"]),
                ASWalkSouthPixels(
                    14,
                    identifier="EVENT_1745_action_queue_async_37_SUBSCRIPT_shift_south_pixels_7"),
                ASFaceNorth(
                    identifier="EVENT_1745_action_queue_async_37_SUBSCRIPT_face_north_8"
                ),
                ASSetAllSpeeds(NORMAL),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Dec(TEMP_70AE),
        SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False),
        UnfreezeAllNPCs(),
        Return(),
        FreezeAllNPCsUntilReturn(
            identifier="EVENT_1745_freeze_all_npcs_until_return_43"
        ),
        Inc(ACTIVE_NPC),
        Inc(TEMP_70AE),
        JmpIfVarEqualsConst(TEMP_70AE, 3, ["EVENT_1745_inc_52"]),
        SummonObjectToCurrentLevelAtMariosCoords(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPlaySound(sound=SO013_COIN, channel=4),
                ASShadowOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetPriority(3),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
                ASAddConstToVar(PRIMARY_TEMP_700C, 2),
                ASMem700CAndConst(0x0004),
                ASMem700CXorConst(0x0004),
                ASFaceEast7C(),
                ASFloatingOff(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x08\xb0\xff")),
                ASWalk1StepFDirection(),
                ASVisibilityOff(),
                ASBPL262728(),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=108, silent=True),
                ASWalk1StepFDirection(),
            ]),
        AddCoins(10),
        Jmp(["EVENT_1745_unfreeze_all_npcs_58"]),
        Inc(ACTIVE_NPC, identifier="EVENT_1745_inc_52"),
        SummonObjectToCurrentLevelAtMariosCoords(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPlaySound(sound=SO094_FROG_COIN, channel=4),
                ASShadowOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
                ASAddConstToVar(PRIMARY_TEMP_700C, 2),
                ASMem700CAndConst(0x0004),
                ASMem700CXorConst(0x0004),
                ASFaceEast7C(),
                ASFloatingOff(),
                ASJumpToHeight(160),
                ASWalkFDirectionSteps(2),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO094_FROG_COIN, channel=4),
                ASJumpToHeight(height=108, silent=True),
                ASWalk1StepFDirection(),
            ]),
        AddFrogCoins(1),
        SetVarToConst(TEMP_70AE, 0),
        UnfreezeAllNPCs(identifier="EVENT_1745_unfreeze_all_npcs_58"),
        Return(),
        FreezeAllNPCsUntilReturn(
            identifier="EVENT_1745_freeze_all_npcs_until_return_60"
        ),
        SetVarToConst(TEMP_70AE, 0),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
                ASVisibilityOn(),
                ASSetAllSpeeds(FAST),
                ASShiftZUpPixels(8),
                ASShiftZDownPixels(8),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
                ASJumpToHeight(108),
                ASPause(32),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
                ASShiftZUpPixels(8),
                ASShiftZDownPixels(8),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=4),
                ASSetAllSpeeds(NORMAL),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
                ASClearSolidityBits(cant_walk_through=True),
                ASSetBit(TEMP_7043_4),
            ]),
        Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Y, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(FAST),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
                ASCompare700CToVar(Y_COORD_1),
                ASJmpIfComparisonResultIsGreaterOrEqual(
                    ["EVENT_1745_action_queue_async_65_SUBSCRIPT_shift_south_pixels_7"]
                ),
                ASWalkNorthPixels(10),
                ASJmp(["EVENT_1745_action_queue_async_65_SUBSCRIPT_face_north_8"]),
                ASWalkSouthPixels(
                    10,
                    identifier="EVENT_1745_action_queue_async_65_SUBSCRIPT_shift_south_pixels_7"),
                ASFaceNorth(
                    identifier="EVENT_1745_action_queue_async_65_SUBSCRIPT_face_north_8"
                ),
                ASSetAllSpeeds(NORMAL),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        UnfreezeAllNPCs(),
        Return(),
    ]
)
