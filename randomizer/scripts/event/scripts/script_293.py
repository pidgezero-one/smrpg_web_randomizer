# pylint: disable=C0301

"""E0293_WALLET_TOAD_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(WALLET_SOLD, ["EVENT_395_run_dialog_37"]),
        JmpIfBitSet(WALLET_RETURNED, ["EVENT_293_run_dialog_45"]),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_293_jmp_if_bit_clear_30"]),
        JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_395_jmp_if_bit_set_0"]),
        PauseActionScript(MEM_70A8, identifier="EVENT_293_pause_action_script_20"),
        SetSyncActionScript(MEM_70A8, A0099_LOOPED_JUMPING),
        RunDialog(
            dialog_id=DI0578_WALLET_GUY_INTRO,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        PauseActionScript(MEM_70A8),
        Pause(1, identifier="EVENT_293_pause_24"),
        JmpIfObjectInAir(MEM_70A8, ["EVENT_293_pause_24"]),
        RunDialog(
            dialog_id=DI0579_WALLET_GUY_PROMISE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        StartAsyncEmbeddedActionScript(
            target=MEM_70A8,
            prefix=0xF1,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASSetSolidityBits(cant_walk_through=True),
            ],
        ),
        SetSyncActionScript(MEM_70A8, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
        Return(),
        JmpIfBitClear(
            REFUSED_TO_RETURN_WALLET,
            ["EVENT_395_jmp_if_bit_set_0"],
            identifier="EVENT_293_jmp_if_bit_clear_30",
        ),
        SetBit(WALLET_RETURNED),
        RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
        Return(),
        RunDialog(
            dialog_id=DI2242_TROOPA_CLIFF_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_293_run_dialog_45",
        ),
        Return(),
    ]
)
