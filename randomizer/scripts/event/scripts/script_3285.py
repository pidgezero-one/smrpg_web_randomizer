# pylint: disable=C0301

"""E3285_SEA_SINGLE_CHEST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_SEA_7055_6, ["EVENT_3285_jmp_if_bit_clear_3"]),
        SetBit(UNKNOWN_SEA_7055_6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R131_SEA_AREA_04_BUNCH_OF_ZEOSTARS, mod_id=32
        ),
        JmpIfBitClear(
            TEMP_7076_0,
            ["EVENT_3285_jmp_to_event_9"],
            identifier="EVENT_3285_jmp_if_bit_clear_3",
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 133, ["EVENT_3285_set_short_8"]),
        SetVarToConst(TIMER_7022, 5),
        Jmp(["EVENT_3285_jmp_to_event_9"]),
        SetVarToConst(TIMER_7022, 40, identifier="EVENT_3285_set_short_8"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3285_jmp_to_event_9"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3285_jmp_to_event_9"]),
        RunEventAsSubroutine(E3905_SEA_STAR_PIECE_SIGNAL),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3285_jmp_to_event_9"),
    ]
)
