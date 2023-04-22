# pylint: disable=C0301

"""E3167_MINES_FINAL_SAVE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW24_MOLEVILLE),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3167_stop_sound_1"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        StopSound(identifier="EVENT_3167_stop_sound_1"),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3167_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3167_ret_26"]),
        RunEventAsSubroutine(E3897_MOLEVILLE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3167_ret_26"),
    ]
)
