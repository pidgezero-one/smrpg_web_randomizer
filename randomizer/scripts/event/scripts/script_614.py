# pylint: disable=C0301

"""E0614_MARRYMORE_SUITE_TIP_BELLHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0986_TIP_PROMPT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_614_pause_15"]),
        Pause(10),
        SetVarToConst(SECONDARY_TEMP_7024, 10),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_614_run_dialog_14"]),
        PlaySound(sound=SO013_COIN, channel=6),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        Dec7000FromCoins(),
        RunDialog(
            dialog_id=DI0988_THANKS_FOR_TIP,
            above_object=NPC_0,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_614_pause_17"]),
        SetBit(TEMP_7042_7),
        Jmp(["EVENT_614_pause_17"]),
        RunDialog(
            dialog_id=DI0987_CANT_AFFORD_TIP,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
            identifier="EVENT_614_run_dialog_14"),
        Pause(10, identifier="EVENT_614_pause_15"),
        RunDialog(
            dialog_id=DI0973_DUPLICATE,
            above_object=NPC_0,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Pause(10, identifier="EVENT_614_pause_17"),
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_614_action_queue_async_29"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASWalk1StepSoutheast(),
                ASWalkSouthwestSteps(2),
                ASVisibilityOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Pause(10),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        ClearBit(TEMP_7042_3),
        SetBit(TEMP_7042_4),
        ClearBit(BELLHOP_UNKNOWN),
        ClearBit(BELLHOP_CALLED),
        Return(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalk1StepNorthwest(),
                ASWalkSouthwestSteps(3),
                ASVisibilityOff(),
            ],
            identifier="EVENT_614_action_queue_async_29"),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        ClearBit(TEMP_7042_3),
        ClearBit(BELLHOP_CALLED),
        ClearBit(BELLHOP_UNKNOWN),
        Return(),
    ]
)
