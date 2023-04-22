# pylint: disable=C0301

"""E0255_EXP_STAR_HIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
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
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_255_ret_13"]),
        SetBit(UNKNOWN_7064_5, identifier="EVENT_255_set_bit_5"),
        SetBit(EXP_STAR_BIT_6),
        UnfreezeAllNPCs(),
        Pause(3),
        CreatePacketAtObjectCoords(
            packet=P031_LEVELUP_TEXT,
            target_npc=MARIO,
            destinations=["EVENT_255_set_bit_5"],
        ),
        PlaySound(sound=SO095_LEVEL_UP_WITH_STAR, channel=6),
        SetVarToConst(TIMER_701E, 64),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_701E
        ),
        Return(identifier="EVENT_255_ret_13"),
    ]
)
