# pylint: disable=C0301

"""E1780_LANDS_END_FLOWER_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MOUSE_RETURNED_TO_MONSTRO, ["EVENT_1780_jmp_if_bit_clear_7_"]),
        SummonObjectToSpecificLevel(NPC_1, R317_LANDS_END_DESERT_AREA_01),
        JmpIfBitClear(
            TEMP_7044_7,
            ["EVENT_1780_jmp_to_event_13"],
            identifier="EVENT_1780_jmp_if_bit_clear_7_",
        ),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1780_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1780_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1780_ret_26"]),
        RunEventAsSubroutine(E3907_LANDS_END_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1780_ret_26"),
    ]
)
