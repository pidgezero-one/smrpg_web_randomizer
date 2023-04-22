# pylint: disable=C0301

"""E3921_SHIP_FIRST_SAVE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3921_jmp_to_event_13"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3921_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3921_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3921_ret_26"]),
        RunEventAsSubroutine(E3906_SHIP_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3921_ret_26"),
    ]
)
