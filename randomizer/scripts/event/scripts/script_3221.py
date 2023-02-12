# E3221_SHIP_3D_MAZE_HIT_BUTTON

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPlaySound(sound=SO009_GREEN_SWITCH, channel=4),
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASShiftZDownPixels(1), ASResetProperties()]
        ),
        SetSyncActionScript(NPC_1, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
        JmpIfBitSet(SHIP_MAZE_PRIZE, ["EVENT_3221_ret_10"]),
        SetVarToConst(X_COORD_1, 26),
        SetVarToConst(Y_COORD_1, 110),
        SetVarToConst(Z_COORD_1, 21),
        Db(bytearray(b"\xfd\xc4")),
        Pause(1, identifier="EVENT_3221_pause_8"),
        RunEventAsSubroutine(E3386_SHIP_3D_MAZE_SPAWN_PRIZE),
        Return(identifier="EVENT_3221_ret_10"),
    ]
)
