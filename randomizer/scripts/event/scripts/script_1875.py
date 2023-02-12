# E1875_KEEP_ROTATING_ROOM_PLATFORM_1

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CompareVarToConst(TEMP_702C, 27),
        JmpIfLoadedMemoryIs0(["EVENT_1875_jmp_if_bit_clear_10"]),
        SetVarToConst(TEMP_702C, 27),
        SetVarToConst(TEMP_70A9, 27),
        SetVarToConst(TEMP_70AA, 28),
        ActionQueueAsync(
            target=MEM_70A9,
            subscript=[
                ASBPL262728(),
                ASDb(bytearray(b"\xfd$\x11\x12")),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
            ],
        ),
        PauseActionScript(NPC_9),
        SetSyncActionScript(MEM_70AA, A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT),
        Pause(2),
        SetSyncActionScript(NPC_9, A0653_SLOW_ROTATING_PLATFORM),
        JmpIfBitClear(
            TEMP_707C_0,
            ["EVENT_1875_ret_13"],
            identifier="EVENT_1875_jmp_if_bit_clear_10",
        ),
        ClearBit(TEMP_707C_0),
        JmpToEvent(E1840_PLATFORM_SUBROUTINE),
        Return(identifier="EVENT_1875_ret_13"),
    ]
)
