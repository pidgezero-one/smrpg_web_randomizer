# pylint: disable=C0301

"""E1649_MOLEVILLE_LIBERATED_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1649_remove_bucket_girl"]),
        JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1649_remove_bucket_girl"]),
        Jmp(["EVENT_1649_set_0"]),
        JmpIfBitClear(
            FIRST_CARBO_COOKIE_GIVEN,
            ["EVENT_1649_set_0"],
            identifier="EVENT_1649_remove_bucket_girl"),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(NPC_7, R108_MOLEVILLE_OUTSIDE),
        SetVarToConst(
            CURRENT_OVERWORLD_MARKER_ID, OW24_MOLEVILLE, identifier="EVENT_1649_set_0"
        ),
        FadeOutMusicToVolume(duration=1, volume=127),
        ActionQueueSync(target=NPC_7, subscript=[ASShiftZDownPixels(5)]),
        JmpIfBitClear(TEMP_7042_1, ["EVENT_1649_jmp_if_bit_set_5"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=0
        ),
        JmpIfBitSet(
            MINECART_CRASH_CUTSCENE_CLEARED,
            ["EVENT_1649_clear_bit_11"],
            identifier="EVENT_1649_jmp_if_bit_set_5"),
        JmpIfBitClear(
            BUCKET_WARP_DIRECTIONAL_BIT, ["EVENT_1649_fade_in_from_black_async_7"]
        ),
        ClearBit(BUCKET_WARP_DIRECTIONAL_BIT),
        ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
        JmpToEvent(E0081_MARIO_LANDS_SUBROUTINE),
        FadeInFromBlack(sync=False, identifier="EVENT_1649_fade_in_from_black_async_7"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1649_star_grant"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1649_star_grant"]),
        RunEventAsSubroutine(E3897_MOLEVILLE_STAR_PIECE_SIGNAL),
        JmpIfBitClear(GAMEBOY_KID_PURCHASE_COMPLETE, ["EVENT_1649_ret_26"]),
        SetVarToConst(PRIMARY_TEMP_7000, 523),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE, identifier="EVENT_1649_star_grant"),
        Return(identifier="EVENT_1649_ret_26"),
        ClearBit(MINECART_CRASH_CUTSCENE_CLEARED, identifier="EVENT_1649_clear_bit_11"),
        JmpIfBitSet(
            OPTIONAL_MINECART_CLEARED, ["EVENT_1649_fade_out_music_to_volume_34"]
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferXYZFSteps(x=0, y=0, z=20, direction=EAST),
            ]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASDb(bytearray(b"\x97\x00")),
                ASVisibilityOn(),
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASSetPriority(3),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
            ]),
        FadeInFromBlack(sync=True),
        PlaySoundBalance(sound=SO019_LONG_FALL, balance=255),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASWalkWestSteps(7),
                ASWalkSouthwestSteps(8),
                ASShiftSouthSteps(5),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASShadowOn(),
                ASSetPriority(3),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(19),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x01\x00\xe0\xff")),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepSouthwest(),
                ASWalk1StepSouthwest(),
                ASShadowOff(),
            ]),
        FadeOutMusicToVolume(duration=1, volume=0),
        FadeOutToBlack(sync=True, duration=15),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASWalk1StepSouthwest(), ASFloatingOff(), ASBPL262728()]),
        RunEventAtReturn(E1650_MOLEVILLE_LIBERATED_EXTERIOR_LOADER_CONTD),
        Return(),
        FadeOutMusicToVolume(
            duration=2, volume=0, identifier="EVENT_1649_fade_out_music_to_volume_34"
        ),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferXYZFSteps(x=0, y=0, z=18, direction=EAST),
            ]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASDb(bytearray(b"\x97\x00")),
                ASClearSolidityBits(cant_pass_walls=True),
                ASVisibilityOn(),
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASSetPriority(3),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
            ]),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(16),
                ASSetWalkingSpeed(FASTER),
                ASWalkSouthwestSteps(4),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASShadowOn(),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASFloatingOn(),
                ASWalkSouthwestSteps(2),
            ]),
        ActionQueueSync(
            target=NPC_8, subscript=[ASSetSolidityBits(cant_pass_walls=True)]
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepSouthwest()]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASStartLoopNTimes(5),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASEndLoop(),
                ASWalkNorthPixels(4),
            ]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO021_RUMBLING, channel=4),
                ASJumpToHeight(64),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASSetAllSpeeds(FAST),
                ASWalkSouthwestSteps(2),
                ASSetAllSpeeds(NORMAL),
                ASWalk1StepSouthwest(),
                ASSetAllSpeeds(SLOW),
                ASWalk1StepSouthwest(),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=False),
                ASSetSolidityBits(cant_walk_through=True),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASJumpToHeight(height=104, silent=True),
                ASWalk1StepNorth(),
                ASFloatingOn(),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASPause(
                    1, identifier="EVENT_1649_action_queue_sync_45_SUBSCRIPT_pause_5"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1649_action_queue_sync_45_SUBSCRIPT_pause_5"]
                ),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASPause(30),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
            ]),
        SetVarToConst(TEMP_7034, 6),
        SetVarToConst(X_COORD_1, 13312),
        SetVarToConst(Y_COORD_1, 5632),
        SetVarToConst(Z_COORD_1, 1024),
        StartLoopNTimes(11),
        Pause(1, identifier="EVENT_1649_pause_51"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1649_pause_51"]
        ),
        Pause(5),
        AddConstToVar(TEMP_7034, 3),
        AddConstToVar(Z_COORD_1, 128),
        EndLoop(),
        UnfreezeCamera(),
        StopMusic(),
        Pause(24),
        PlayMusicAtDefaultVolume(M33_MOLEVILLE),
        ActionQueueAsync(target=NPC_3, subscript=[ASWalk1StepSoutheast()]),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNorthwest()]),
        CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1100_MINECART_SCORE,
            above_object=NPC_8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
        RunDialogForDuration(
            dialog_id=DI1101_MINECART_HIGH_SCORE, duration=0, sync=False
        ),
        CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
        Compare7000ToVar(TEMP_702E),
        JmpIfComparisonResultIsLesser(["EVENT_1649_run_dialog_duration_72"]),
        RunDialogForDuration(
            dialog_id=DI1102_MINECART_DID_NOT_SET_PB, duration=1, sync=False
        ),
        Jmp(["EVENT_1649_clear_bit_90"]),
        RunDialogForDuration(
            dialog_id=DI1103_MINECART_SET_PB,
            duration=1,
            sync=False,
            identifier="EVENT_1649_run_dialog_duration_72"),
        JmpIfBitClear(MINECART_INITIATE_FREEPLAY, ["EVENT_1649_clear_bit_90"]),
        SetSyncActionScript(NPC_3, A0650_BLUE_CLOUD_MOVEMENT),
        RunDialog(
            dialog_id=DI1116_WON_AFTER_WAGER,
            above_object=NPC_8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=2, sprite_offset=3, is_sequence=True, looping=True
                )
            ]),
        ActionQueueAsync(target=NPC_3, subscript=[ASSetSequenceSpeed(FAST)]),
        StartLoopNTimes(4),
        AddCoins(10),
        PlaySound(sound=SO013_COIN, channel=6),
        Pause(1, identifier="EVENT_1649_pause_81"),
        Set70107015ToObjectXYZ(NPC_3),
        AddConstToVar(X_COORD_1, 160),
        AddConstToVar(Z_COORD_1, 352),
        CreatePacketAt7010(
            packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_1649_pause_81"]
        ),
        Pause(30),
        EndLoop(),
        ActionQueueAsync(target=NPC_3, subscript=[ASSetSequenceSpeed(NORMAL)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(15),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASEndLoop(),
                ASSetSpriteSequence(
                    index=10, sprite_offset=2, is_sequence=True, looping=False
                ),
                ASPause(60),
                ASResetProperties(),
            ]),
        ClearBit(MINECART_INITIATE_FREEPLAY, identifier="EVENT_1649_clear_bit_90"),
        Return(),
    ]
)
