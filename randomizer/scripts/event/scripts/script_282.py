# pylint: disable=C0301

"""E0282_UNKNOWN_PIPE_VAULT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7049_0),
        MoveScriptToBackgroundThread2(),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASJumpToHeight(height=0, silent=True),
            ]),
        JmpIfBitSet(TEMP_709C_3, ["EVENT_282_clear_bit_6"]),
        FadeInFromBlack(sync=False),
        ClearBit(TEMP_709C_3, identifier="EVENT_282_clear_bit_6"),
        Return(),
    ]
)
