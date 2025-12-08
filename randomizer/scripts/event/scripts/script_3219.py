# pylint: disable=C0301

"""E3219_SHIP_BARREL_PUZZLE_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        SetSyncActionScript(MEM_70A8, A0336_SHIP_BARREL_PUZZLE_BUTTON),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASShiftZDownPixels(2),
                ASResetProperties(),
                ASSetSolidityBits(cant_pass_npcs=True),
            ]),
        Inc(TEMP_70AE),
        JmpIfVarEqualsConst(TEMP_70AE, 2, ["EVENT_3219_action_queue_async_6"]),
        Return(),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASIncPaletteRowBy(15)],
            identifier="EVENT_3219_action_queue_async_6"),
        SetSyncActionScript(NPC_3, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
        JmpIfBitSet(UNKNOWN_707D_5, ["EVENT_3219_action_queue_sync_15"]),
        SetVarToConst(X_COORD_1, 17),
        SetVarToConst(Y_COORD_1, 18),
        SetVarToConst(Z_COORD_1, 21),
        Db(bytearray(b"\xfd\xc4")),
        Pause(1, identifier="EVENT_3219_pause_13"),
        RunEventAsSubroutine(E3389_SHIP_BARREL_PUZZLE_SPAWN_PRIZE),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASObjectMemorySetBit(arg_1=0x30, bits=[4])],
            identifier="EVENT_3219_action_queue_sync_15"),
        SetSyncActionScript(NPC_1, A0336_SHIP_BARREL_PUZZLE_BUTTON),
        SetSyncActionScript(NPC_2, A0336_SHIP_BARREL_PUZZLE_BUTTON),
        Return(),
    ]
)
