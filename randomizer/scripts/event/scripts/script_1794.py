# pylint: disable=C0301

"""E1794_LANDS_END_BUY_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1794_action_queue_sync_77"]),
        JmpIfBitSet(LANDS_END_CHEST_1_USED, ["EVENT_1794_jmp_if_bit_set_26"]),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 400),
        JmpIfComparisonResultIsLesser(["EVENT_1794_run_dialog_70"]),
        RunDialog(
            dialog_id=DI1223_SHAMAN_SALESMAN_400_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBSelected(["EVENT_1794_pause_20"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSequenceLoopingOn(),
                ASPause(30),
                ASSetSequenceSpeed(VERY_SLOW),
            ]),
        SetVarToConst(PRIMARY_TEMP_7000, 400),
        Dec7000FromCoins(),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        SetVarToConst(TEMP_70AA, 38),
        JmpToSubroutine(["EVENT_1794_action_queue_sync_55"]),
        SetBit(LANDS_END_CHEST_1_PAID),
        Return(),
        Pause(10, identifier="EVENT_1794_pause_20"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
        JmpIfBitSet(
            LANDS_END_CHEST_2_REQUESTED,
            ["EVENT_1794_store_coin_amount_7000_36"],
            identifier="EVENT_1794_jmp_if_bit_set_26"),
        RunDialog(
            dialog_id=DI1224_SHAMAN_SALESMAN_2ND_PROMPT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBSelected(["EVENT_1794_pause_20"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        RunDialog(
            dialog_id=DI1226_SHAMAN_SALESMAN_LEAVES,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        SetBit(LANDS_END_CHEST_2_REQUESTED),
        JmpToSubroutine(["EVENT_1794_set_72"]),
        RemoveObjectFromSpecificLevel(
            NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        Return(),
        StoreCoinCountTo7000(identifier="EVENT_1794_store_coin_amount_7000_36"),
        CompareVarToConst(PRIMARY_TEMP_7000, 800),
        JmpIfComparisonResultIsLesser(["EVENT_1794_run_dialog_70"]),
        RunDialog(
            dialog_id=DI1227_SHAMAN_SALESMAN_800_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBSelected(["EVENT_1794_clear_bit_53"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSequenceLoopingOn(),
                ASPause(30),
                ASSetSequenceSpeed(VERY_SLOW),
            ]),
        SetVarToConst(PRIMARY_TEMP_7000, 800),
        Dec7000FromCoins(),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        SetVarToConst(TEMP_70AA, 39),
        JmpToSubroutine(["EVENT_1794_action_queue_sync_55"]),
        SetBit(LANDS_END_CHEST_2_PAID),
        ClearBit(LANDS_END_CHEST_2_REQUESTED),
        RemoveObjectFromSpecificLevel(
            NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        Return(),
        ClearBit(LANDS_END_CHEST_2_REQUESTED, identifier="EVENT_1794_clear_bit_53"),
        Jmp(["EVENT_1794_pause_20"]),
        ActionQueueSync(
            target=NPC_16,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(112),
                ASStartLoopNTimes(11),
                ASTurnClockwise45DegreesNTimes(6),
                ASPause(1),
                ASEndLoop(),
            ],
            identifier="EVENT_1794_action_queue_sync_55"),
        Pause(20),
        SetVarToConst(TEMP_7034, 6),
        Set70107015ToObjectXYZ(MEM_70AA),
        PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=6),
        StartLoopNTimes(8),
        Pause(1, identifier="EVENT_1794_pause_61"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1794_pause_61"]
        ),
        Pause(5),
        AddConstToVar(TEMP_7034, 3),
        AddConstToVar(Z_COORD_1, 64),
        EndLoop(),
        ActionQueueAsync(
            target=MEM_70AA,
            subscript=[
                ASStartLoopNTimes(4),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(2),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(8),
                ASEndLoop(),
            ]),
        SetSyncActionScript(MEM_70AA, A0014_FLOATING_CHEST),
        Jmp(["EVENT_1794_set_72"]),
        RunDialog(
            dialog_id=DI1222_SHAMAN_SALESMAN_NOT_ENOUGH_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1794_run_dialog_70"),
        Return(),
        SetVarToConst(TEMP_70AA, 36, identifier="EVENT_1794_set_72"),
        ActionQueueAsync(
            target=MEM_70AA,
            subscript=[
                ASPlaySound(sound=SO059_HOVERING_FROGFUCIUS, channel=4),
                ASSequencePlaybackOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(SLOW),
                ASShiftZUpSteps(2),
                ASStartLoopNTimes(3),
                ASPause(1),
                ASVisibilityOn(),
                ASPause(6),
                ASVisibilityOff(),
                ASEndLoop(),
                ASPause(
                    1, identifier="EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_11"
                ),
                ASSetVarToConst(TEMP_7034, 65535),
                ASCreatePacketAtObjectCoords(
                    packet=P032_BLUE_CLOUD,
                    target_npc=MEM_70AA,
                    destinations=[
                        "EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_11"
                    ]),
                ASPlaySound(sound=SO161_GHOST, channel=4),
            ],
            identifier="EVENT_1794_action_queue_async_73"),
        Return(),
        ActionQueueSync(
            target=NPC_16,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(128),
                ASStartLoopNTimes(11),
                ASPause(4),
                ASTurnClockwise45DegreesNTimes(2),
                ASEndLoop(),
                ASSetSolidityBits(bit_4=True, cant_walk_through=True),
            ],
            identifier="EVENT_1794_action_queue_sync_77"),
        Return(),
    ]
)
