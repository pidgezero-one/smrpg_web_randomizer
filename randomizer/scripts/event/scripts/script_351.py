# pylint: disable=C0301

"""E0351_GAMEBOY_KID"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_351_jmp_if_bit_set_0_"]),
        JmpIfBitSet(
            BEETLEMANIA_UNLOCKED,
            ["EVENT_351_run_dialog_42"],
            identifier="EVENT_351_jmp_if_bit_set_0",
        ),
        JmpIfRandom1of2(["EVENT_351_run_dialog_7"]),
        RunDialog(
            dialog_id=DI3733_GAMEBOY_KID,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI3732_GAMEBOY_KID,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_351_run_dialog_7",
        ),
        Return(),
        JmpIfBitSet(
            STAR_PIECE_GRANT_DIRECTIONAL_BIT,
            ["EVENT_351_jmp_if_bit_set_0"],
            identifier="EVENT_351_jmp_if_bit_set_0_",
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASDb(bytearray(b"\xfd$\x17\x00")),
                ASMem700CAndConst(0x00C0),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C, 64, ["EVENT_351_run_event_as_subroutine_29"]
                ),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=4, y=0, z=0, direction=EAST),
                ASJmp(["EVENT_351_run_event_as_subroutine_29"]),
            ],
        ),
        RunEventAsSubroutine(
            E3587_SET_70AE_TO_70A8, identifier="EVENT_351_run_event_as_subroutine_29"
        ),
        RunDialog(
            dialog_id=DI3738_GAMEBOY_KID_SELL_PROMPT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_351_pause_52"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        SetVarToConst(SECONDARY_TEMP_7024, 500),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_351_run_dialog_56"]),
        PlaySound(sound=SO013_COIN, channel=6),
        SetVarToConst(PRIMARY_TEMP_7000, 500),
        Dec7000FromCoins(),
        SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Jmp(["EVENT_351_action_queue_async_58"]),
        RunDialog(
            dialog_id=DI3742_GAMEBOY_KID_TUTORIAL_PROMPT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_351_run_dialog_42",
        ),
        JmpIfDialogOptionBSelected(["EVENT_351_pause_48"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        RunDialog(
            dialog_id=DI3744_BEETLEMANIA_TUTORIAL,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Jmp(["EVENT_351_action_queue_async_58"]),
        Pause(10, identifier="EVENT_351_pause_48"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Jmp(["EVENT_351_action_queue_async_58"]),
        Pause(10, identifier="EVENT_351_pause_52"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Jmp(["EVENT_351_action_queue_async_58"]),
        RunDialog(
            dialog_id=DI3741_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_351_run_dialog_56",
        ),
        Jmp(["EVENT_351_action_queue_async_58"]),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASTransferToXYZF(x=9, y=91, z=0, direction=EAST),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
            identifier="EVENT_351_action_queue_async_58",
        ),
        Return(),
    ]
)
