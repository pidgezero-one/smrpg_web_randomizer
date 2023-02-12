# E3148_ROSE_WAY_MAIN_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_707C_1),
        SummonObjectToSpecificLevel(NPC_1, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_2, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_3, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_4, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SetVarToConst(ROSE_WAY_7038, 0),
        SetVarToConst(ROSE_WAY_703A, 0),
        SetVarToConst(ROSE_WAY_703C, 0),
        SetVarToConst(ROSE_WAY_703E, 0),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3148_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3148_ret_26"]),
        RunEventAsSubroutine(E3894_ROSE_WAY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3148_ret_26"),
    ]
)
