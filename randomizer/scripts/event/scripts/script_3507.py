# pylint: disable=C0301

"""E3507_BOOSTER_HILL_2ND_PASS_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7034, 16),
        SetVarToConst(TEMP_7026, 1),
        SetVarToRandom(TEMP_702C, 6),
        Inc(TEMP_702C),
        SetVarToConst(TEMP_70AF, 3),
        FreezeCamera(),
        ActionQueueSync(
            target=MARIO, subscript=[ASTransferToXYZF(x=11, y=67, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=LAYER_3,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNorthwestSteps(18)]),
        FadeInFromBlack(sync=False),
        SetVarToConst(TEMP_70AE, 26),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetAllSpeeds(FAST), ASWalkNorthwestSteps(8)]
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=11, y=67, z=0, direction=EAST),
                ASSetPriority(3),
                ASVisibilityOn(),
                ASSetAllSpeeds(FAST),
                ASWalkNorthwestSteps(7),
                ASJumpToHeight(64),
            ]),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSoutheast()]),
        RunDialog(
            dialog_id=DI1199_TOAD_WARNS_YOU_TO_LEAVE_EMPTY_HILL,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_3507_set_7000_to_70A0_short_mem_36"]),
        Pause(10, identifier="EVENT_3507_pause_28"),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        RunDialog(
            dialog_id=DI1200_TOAD_TAKES_YOU_OUT_OF_HILL,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        ActionQueueSync(
            target=NPC_6, subscript=[ASWalkSoutheastSteps(7), ASVisibilityOff()]
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASWalkSoutheastSteps(7), ASVisibilityOff()]
        ),
        RunEventAtReturn(E3510_BOOSTER_HILL_EXIT_TO_WORLD_MAP),
        Return(),
        CopyVarToVar(
            from_var=BOOSTER_HILL_70B1,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3507_set_7000_to_70A0_short_mem_36"),
        CompareVarToConst(PRIMARY_TEMP_7000, 8),
        JmpIfComparisonResultIsLesser(["EVENT_3507_pause_48"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        JmpIfBitSet(UNKNOWN_704E_2, ["EVENT_3507_run_dialog_45"]),
        RunDialog(
            dialog_id=DI1203_TOAD_TELLS_YOU_THERES_NOTHING_LEFT,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_3507_pause_48"]),
        Jmp(["EVENT_3507_pause_28"]),
        RunDialog(
            dialog_id=DI1202_TOAD_TELLS_YOU_THERES_NO_FLOWERS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3507_run_dialog_45"),
        JmpIfDialogOptionBSelected(["EVENT_3507_pause_48"]),
        Jmp(["EVENT_3507_pause_28"]),
        Pause(10, identifier="EVENT_3507_pause_48"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        RunDialog(
            dialog_id=DI1201_WHATEVER,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASResetProperties(),
                ASWalkSoutheastSteps(6),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASSequenceLoopingOn(),
            ]),
        RunBackgroundEvent(
            event_id=E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND,
            return_on_level_exit=True,
            bit_6=True),
        SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
        SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
        SetSyncActionScript(LAYER_3, A0705_BOOSTER_HILL_LAYER_3),
        SetBit(UNKNOWN_707B_4),
        RunEventAtReturn(E3502_BOOSTER_HILL_END),
        Return(),
    ]
)
