# pylint: disable=C0301

"""E2648_CASINO_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(DIRECTIONAL_7046_1),
        ClearBit(DIRECTIONAL_7046_0),
        ClearBit(DIRECTIONAL_7045_7),
        SetBit(UNKNOWN_CASINO_7059_1),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2648_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2648_ret_26"]),
        RunEventAsSubroutine(E3910_CASINO_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2648_ret_26"),
    ]
)
