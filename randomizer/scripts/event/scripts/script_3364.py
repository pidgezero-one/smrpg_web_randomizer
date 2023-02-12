# E3364_KEEP_LOGIC_GAME_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShiftXYPixels(x=250, y=253),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(target=MARIO, subscript=[ASShiftNortheastSteps(5)]),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftNortheastSteps(2)]),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        SetBit(TEMP_7044_7),
        SetVarToConst(SECONDARY_TEMP_7024, 1),
        SetVarToConst(TEMP_7026, 2),
        SetVarToConst(TEMP_7028, 3),
        SetVarToConst(TEMP_702A, 4),
        StartLoopNTimes(18),
        JmpIfRandom1of2(["EVENT_3364_jmp_if_random_above_66_21"]),
        JmpIfRandom2of3(["EVENT_3364_db_17", "EVENT_3364_db_19"]),
        Db(bytearray(b"\xbd\x12\x13")),
        Jmp(["EVENT_3364_end_loop_27"]),
        Db(bytearray(b"\xbd\x12\x14"), identifier="EVENT_3364_db_17"),
        Jmp(["EVENT_3364_end_loop_27"]),
        Db(bytearray(b"\xbd\x12\x15"), identifier="EVENT_3364_db_19"),
        Jmp(["EVENT_3364_end_loop_27"]),
        JmpIfRandom2of3(
            ["EVENT_3364_db_24", "EVENT_3364_db_26"],
            identifier="EVENT_3364_jmp_if_random_above_66_21",
        ),
        Db(bytearray(b"\xbd\x13\x14")),
        Jmp(["EVENT_3364_end_loop_27"]),
        Db(bytearray(b"\xbd\x13\x15"), identifier="EVENT_3364_db_24"),
        Jmp(["EVENT_3364_end_loop_27"]),
        Db(bytearray(b"\xbd\x14\x15"), identifier="EVENT_3364_db_26"),
        EndLoop(identifier="EVENT_3364_end_loop_27"),
        PlayMusicAtDefaultVolume(M36_EXPLANATION),
        Return(),
    ]
)
