# E0641_MARRYMORE_ANTECHAMBER_LOADER_EXTENSION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASTransferXYZFPixels(x=0, y=3, z=0, direction=EAST),
            ],
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            mod_id=0,
        ),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_641_run_event_as_subroutine_59"]),
        FadeInFromBlack(sync=False),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_256_ret_0"]),
        SetBit(SANCTUARY_LOCKED),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_641_run_event_as_subroutine_59",
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_641_ret_60"]),
        RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_641_ret_60"),
    ]
)
