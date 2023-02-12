# E0670_MARRYMORE_UNOCCUPIED_EXTERIOR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set0158Bit7Offset(),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(3)]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
                ASSetPriority(3),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
                ASSetPriority(3),
            ],
        ),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_8, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_9, subscript=[ASSetPriority(3)]),
        RememberLastObject(),
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        ClearBit(TEMP_7042_3),
        ClearBit(TEMP_7042_4),
        ClearBit(TEMP_7042_5),
        ClearBit(TEMP_7042_6),
        ClearBit(TEMP_7042_7),
        SetVarToConst(TEMP_70AC, 0),
        SetVarToConst(TEMP_70B8, 0),
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        ClearBit(EMPLOYMENT_704C_2),
        ClearBit(EMPLOYMENT_704C_3),
        ClearBit(BELLHOP_CALLED),
        ClearBit(MARRYMORE_UNKNOWN_709F_6),
        FadeOutMusicToVolume(duration=1, volume=127),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_670_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_670_ret_26"]),
        RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_670_ret_26"),
    ]
)
