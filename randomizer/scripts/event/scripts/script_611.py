# pylint: disable=C0301

"""E0611_MARRYMORE_INN_LOBBY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=1, volume=96),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_611_action_queue_sync_92"]),
        JmpIfBitSet(TEMP_7042_6, ["EVENT_611_jmp_if_bit_clear_23"]),
        JmpIfBitSet(TEMP_7042_5, ["EVENT_611_action_queue_async_19"]),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_611_jmp_if_bit_set_11"]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_611_run_event_as_subroutine_8"]),
        FadeInFromBlack(sync=False),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_611_run_event_as_subroutine_8",
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_611_jmp_if_bit_set_9"]),
        RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
        JmpIfBitSet(
            TEMP_7044_4,
            ["EVENT_611_jmp_if_bit_set_16"],
            identifier="EVENT_611_jmp_if_bit_set_9",
        ),
        Return(),
        JmpIfBitSet(
            TEMP_7042_4,
            ["EVENT_611_jmp_if_bit_set_13"],
            identifier="EVENT_611_jmp_if_bit_set_11",
        ),
        RemoveObjectFromCurrentLevel(NPC_5),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_611_run_event_as_subroutine_8"],
            identifier="EVENT_611_jmp_if_bit_set_13",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfBitSet(
            EMPLOYMENT_704C_2,
            ["EVENT_256_ret_0"],
            identifier="EVENT_611_jmp_if_bit_set_16",
        ),
        RunBackgroundEvent(
            event_id=E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES,
            return_on_level_exit=True,
        ),
        Return(),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=6, y=62, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_611_action_queue_async_19",
        ),
        FadeInFromBlack(sync=False),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_611_run_event_as_subroutine_8"]),
        Return(),
        JmpIfBitClear(
            TEMP_7042_5,
            ["EVENT_611_jmp_if_bit_clear_25"],
            identifier="EVENT_611_jmp_if_bit_clear_23",
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=6, y=62, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        JmpIfBitClear(
            TEMP_704C_0,
            ["EVENT_611_jmp_if_bit_clear_27"],
            identifier="EVENT_611_jmp_if_bit_clear_25",
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=6, y=63, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        JmpIfBitClear(
            TEMP_7042_5,
            ["EVENT_611_jmp_if_bit_set_13"],
            identifier="EVENT_611_jmp_if_bit_clear_27",
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepSouthwest()]),
        Pause(10),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Inc(PRIMARY_TEMP_7000),
        JmpIfBitSet(MARRYMORE_UNKNOWN_709F_6, ["EVENT_611_run_dialog_76"]),
        RunDialog(
            dialog_id=DI2509_100_COINS_FOR_EVERY_EXTRA_DAY,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        Dec(SECONDARY_TEMP_7024),
        SetVarToConst(TEMP_7026, 0),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 100),
        JmpIfComparisonResultIsLesser(["EVENT_611_set_bit_58"]),
        SetVarToConst(PRIMARY_TEMP_7000, 100),
        Dec7000FromCoins(),
        Inc(TEMP_7026),
        PlaySound(sound=SO013_COIN, channel=6),
        Pause(20),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(120),
                ASResetProperties(),
            ],
        ),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1003_THEY_TOOK_ALL_COINS,
            above_object=Bowser,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False,
            bit_6=True,
        ),
        RememberLastObject(),
        SetBit(TEMP_7043_1),
        ClearBit(TEMP_7042_6),
        SetSyncActionScript(NPC_1, A0323_MARRYMORE_INNKEEPER_OVERSTAY_TAKE_COINS),
        SetSyncActionScript(NPC_5, A0891_MARRYMORE_BELLHOP_AFTER_PAYING_FOR_OVERSTAY),
        SetVarToConst(TEMP_70AC, 0),
        Return(),
        SetBit(TEMP_704C_0, identifier="EVENT_611_set_bit_58"),
        ClearBit(TEMP_7042_6),
        RunDialog(
            dialog_id=DI1002_DUPLICATE,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        DecVarFrom7000(TEMP_7026),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                )
            ],
        ),
        SetSyncActionScript(
            NPC_1,
            A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK,
            identifier="EVENT_611_set_action_script_sync_65",
        ),
        FadeOutToBlack(sync=True, duration=90),
        PauseScriptUntilEffectDone(),
        EnterArea(
            room_id=R007_MARRYMORE_INN_1F, face_direction=SOUTHEAST, x=3, y=55, z=0
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=6, y=63, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        FadeInFromBlack(sync=True, duration=90),
        PauseScriptUntilEffectDone(),
        Pause(120),
        RunBackgroundEvent(
            event_id=E0617_MARIO_AS_BELLHOP_MAIN_EVENT, return_on_level_exit=True
        ),
        Return(),
        RunDialog(
            dialog_id=DI2479_100_COINS_FOR_EVERY_EXTRA_DAY,
            above_object=NPC_1,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_611_run_dialog_76",
        ),
        RunDialog(
            dialog_id=DI2480_CANT_AFFORD_HOTEL_DEBT,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        StoreCoinCountTo7000(),
        Dec7000FromCoins(),
        StoreFrogCoinCountTo7000(),
        Dec7000FromFrogCoins(),
        PlaySound(sound=SO013_COIN, channel=6),
        Pause(60),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        Pause(60),
        RunDialog(
            dialog_id=DI2478_LOST_ALL_COINS_AND_FROG_COINS,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetBit(TEMP_704C_0),
        ClearBit(TEMP_7042_6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                )
            ],
        ),
        SetVarToConst(TEMP_70AC, 200),
        Jmp(["EVENT_611_set_action_script_sync_65"]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=6, y=63, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
            identifier="EVENT_611_action_queue_sync_92",
        ),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_611_jmp_if_bit_set_104"]),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_611_jmp_if_bit_set_104"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_611_action_queue_sync_100"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_611_action_queue_async_103"]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=4, y=60, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
        ),
        Jmp(["EVENT_611_jmp_if_bit_set_104"]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASTransferToXYZF(x=4, y=60, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_611_action_queue_sync_100",
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASTransferToXYZF(x=4, y=59, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        Jmp(["EVENT_611_jmp_if_bit_set_104"]),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=4, y=60, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
            identifier="EVENT_611_action_queue_async_103",
        ),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_611_run_event_as_subroutine_8"],
            identifier="EVENT_611_jmp_if_bit_set_104",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
