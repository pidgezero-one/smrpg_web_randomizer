# E1779_LANDS_END_UNDERGROUND_1_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_1779_jmp_to_event_13"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1779_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1779_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1779_ret_26"]),
        RunEventAsSubroutine(E3907_LANDS_END_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1779_ret_26"),
    ]
)
