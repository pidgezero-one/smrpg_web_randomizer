# E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1604_disable_trigger_0"]),
        Return(),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_1604_disable_trigger_0"),
        StartAsyncEmbeddedActionScript(
            target=MEM_70A8,
            prefix=0xF1,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        SetSyncActionScript(MEM_70A8, A1022_HIT_BY_EXP_STAR),
        IncEXPByPacket(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1604_ret_78_cancel"]),
        SetBit(UNKNOWN_7064_5, identifier="EVENT_1604_set_bit_5"),
        SetBit(EXP_STAR_BIT_6),
        UnfreezeAllNPCs(),
        Pause(3),
        CreatePacketAtObjectCoords(
            packet=P031_LEVELUP_TEXT,
            object=MARIO,
            destinations=["EVENT_1604_set_bit_5"],
        ),
        PlaySound(sound=SO095_LEVEL_UP_WITH_STAR, channel=6),
        SetVarToConst(TIMER_701E, 64),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_701E
        ),
        EndAll(identifier="EVENT_1604_ret_78_cancel"),
    ]
)
