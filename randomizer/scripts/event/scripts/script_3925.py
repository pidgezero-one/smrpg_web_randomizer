# pylint: disable=C0301

"""E3925_FACTORY_SAVE_ROOM_LOADERS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3925_jmp_to_event_13"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3925_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3925_star_grant"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3925_star_grant"]),
        RunEventAsSubroutine(E3915_FACTORY_STAR_PIECE_SIGNAL),
        JmpIfBitClear(GAMEBOY_KID_PURCHASE_COMPLETE, ["EVENT_3925_ret_26"]),
        JmpToEvent(
            E0168_BOSS_GRANT_STAR_PIECE_CONTAINER, identifier="EVENT_3925_star_grant"
        ),
        Return(identifier="EVENT_3925_ret_26"),
    ]
)
