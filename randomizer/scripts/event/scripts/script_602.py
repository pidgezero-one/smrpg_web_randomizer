# pylint: disable=C0301

"""E0602_MARRYMORE_INN_MANAGER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_602_jmp_if_bit_set_137"]),
        JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_602_jmp_if_bit_set_137"]),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_602_run_dialog_135"]),
        JmpIfBitSet(TEMP_7042_5, ["EVENT_602_run_dialog_133"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_602_run_dialog_133"]),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_602_run_dialog_61"]),
        RunDialog(
            dialog_id=DI2470_MARRYMORE_HOTEL_MENU,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_602_run_dialog_18", "EVENT_602_run_dialog_59"]
        ),
        CloseDialog(),
        JmpToEvent(E0646_MARRYMORE_SHOP_EVENT_CONTAINER),
        RunDialog(
            dialog_id=DI2508_MARRYMORE_HOTEL_ROOM_CHOICE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_18"),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_602_set_short_31", "EVENT_602_run_dialog_59"]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 10),
        ClearBit(UNKNOWN_7049_4),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_29"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        Dec7000FromCoins(),
        RunDialog(
            dialog_id=DI0974_ENJOY_YOUR_STAY,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        SetBit(MARRYMORE_REGULAR_INN),
        Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
        RunDialog(
            dialog_id=DI2475_CANT_AFFORD_MARRYMORE_HOTEL,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_29"),
        Return(),
        SetVarToConst(SECONDARY_TEMP_7024, 200, identifier="EVENT_602_set_short_31"),
        ClearBit(UNKNOWN_7049_4),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_29"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        Dec7000FromCoins(),
        CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_602_set_bit_63"]),
        Inc(MARRYMORE_SUITE_LEGAL_COUNT),
        SetBit(TEMP_7043_0, identifier="EVENT_602_set_bit_63"),
        CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI2473_STAYED_X_TIMES_IN_SUITE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        UnsyncDialog(),
        RememberLastObject(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 255, ["EVENT_602_set_7010_to_object_xyz_72"]
        ),
        RunEventAsSubroutine(E0708_MARRYMORE_TIP_DECISION_SUBROUTINE),
        Db(bytearray(b"\xc7\x99"), identifier="EVENT_602_set_7010_to_object_xyz_72"),
        CompareVarToConst(X_COORD_1, 5),
        JmpIfComparisonResultIsGreaterOrEqual(
            ["EVENT_602_start_embedded_action_script_sync_F1_81"]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASFaceNortheast(), ASPause(30), ASFaceSoutheast()]
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_5,
            prefix=0xF1,
            subscript=[
                ASPause(30),
                ASSetSequenceSpeed(FAST),
                ASFixedFCoordOff(),
                ASWalkNortheastSteps(2),
                ASWalkSoutheastSteps(4),
                ASWalkSouthwestSteps(2),
                ASSetSequenceSpeed(SLOW),
            ]),
        Jmp(["EVENT_602_set_bit_55"]),
        StartSyncEmbeddedActionScript(
            target=NPC_5,
            prefix=0xF1,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASFixedFCoordOff(),
                ASWalk1StepNorthwest(),
                ASWalkToXYCoords(x=6, y=61),
                ASWalkNorthwestSteps(2),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(SLOW),
            ],
            identifier="EVENT_602_start_embedded_action_script_sync_F1_81"),
        SetBit(TEMP_7042_0, identifier="EVENT_602_set_bit_55"),
        SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
        SetSyncActionScript(NPC_5, A0301_MARRYMORE_BELLHOP_WHILE_PLAYER_WORKING),
        Return(),
        RunDialog(
            dialog_id=DI0976_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_59"),
        Return(),
        RunDialog(
            dialog_id=DI0973_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_61"),
        Return(),
        RunDialog(
            dialog_id=DI0998_THANK_YOU_VERY_MUCH,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_133"),
        Return(),
        RunDialog(
            dialog_id=DI1004_BREAK_EVERY_BONE_IN_YOUR_BODY,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_135"),
        Return(),
        JmpIfBitSet(
            GUEST_DROPPED_OFF,
            ["EVENT_602_run_dialog_157"],
            identifier="EVENT_602_jmp_if_bit_set_137"),
        Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_602_run_dialog_162"]),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Dec(PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_602_run_dialog_149"]),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        RunDialog(
            dialog_id=DI1019_NOT_OFF_THE_HOOK,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=3, y=55),
                ASFaceSoutheast(),
                ASPause(30),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASResetProperties(),
                ASSetSequenceSpeed(SLOW),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSequenceLoopingOn(),
            ]),
        ClearBit(EMPLOYMENT_704C_2),
        RunBackgroundEvent(
            event_id=E0617_MARIO_AS_BELLHOP_MAIN_EVENT, return_on_level_exit=True
        ),
        Return(),
        RunDialog(
            dialog_id=DI1020_FINISHED_WORKING_AT_MARRYMORE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_149"),
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        ClearBit(EMPLOYMENT_704C_2),
        SetVarToConst(TEMP_70AC, 0),
        SetVarToConst(TEMP_70B8, 0),
        SetBit(EMPLOYMENT_704C_3),
        Return(),
        RunDialog(
            dialog_id=DI1014_SEE_GUEST_OUT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_157"),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_256_ret_0"]),
        RunBackgroundEvent(
            event_id=E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES,
            return_on_level_exit=True),
        SetBit(TEMP_7044_4),
        Return(),
        RunDialog(
            dialog_id=DI1021_MARRYMORE_INNKEEPER_TELLS_YOU_TO_GO_BEHIND_COUNTER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_602_run_dialog_162"),
        Return(),
    ]
)
