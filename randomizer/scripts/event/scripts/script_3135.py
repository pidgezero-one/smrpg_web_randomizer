# pylint: disable=C0301

"""E3135_SEWERS_GENERIC_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_5),
        SetVarToConst(TIMER_701C, 300),
        StopBackgroundEvent(TIMER_701C),
        JmpIfVarEqualsConst(
            CURRENT_OVERWORLD_MARKER_ID,
            OW14_KERO_SEWERS,
            ["EVENT_3135_jmp_if_bit_set_7"]),
        JmpToSubroutine(["EVENT_3134_summon_to_level_15"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW14_KERO_SEWERS),
        Jmp(["EVENT_3135_jmp_if_bit_clear_9"]),
        JmpIfBitSet(
            TEMP_7042_0,
            ["EVENT_3135_jmp_if_bit_clear_9"],
            identifier="EVENT_3135_jmp_if_bit_set_7"),
        JmpToSubroutine(["EVENT_3134_summon_to_level_15"]),
        JmpIfBitClear(
            SEWER_WATER_LEVEL,
            ["EVENT_3135_reset_priority_set_14"],
            identifier="EVENT_3135_jmp_if_bit_clear_9"),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 62, ["EVENT_3135_run_event_as_subroutine_15"]
        ),
        PrioritySet(
            mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[]
        ),
        Jmp(["EVENT_3135_run_event_as_subroutine_15"]),
        ResetPrioritySet(identifier="EVENT_3135_reset_priority_set_14"),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3135_run_event_as_subroutine_15"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER,
            identifier="EVENT_3135_run_event_as_subroutine_15"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3135_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3135_ret_26"]),
        RunEventAsSubroutine(E3891_SEWERS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3135_ret_26"),
    ]
)
