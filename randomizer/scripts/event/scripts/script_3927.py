# pylint: disable=C0301

"""E3927_NIMBUS_CASTLE_EXIT_HALLWAY_SAVE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0838_NIMBUS_CASTLE_FIRST_POST_THRONE_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3927_jmp_to_event_13"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3927_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3927_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3927_ret_26"]),
        RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3927_ret_26"),
    ]
)
