# pylint: disable=C0301

"""E1753_LANDS_END_FINAL_WHIRLPOOL_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R319_LANDS_END_DESERT_AREA_06,
            ["EVENT_1753_set_7000_to_7000_short_mem_9"],
        ),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 20, ["EVENT_1754_run_event_as_subroutine_3"]
        ),
        RunEventAsSubroutine(
            E1544_SAND_WHIRLPOOL, identifier="EVENT_1753_run_event_as_subroutine_3"
        ),
        EnterArea(
            room_id=R403_LANDS_END_DESERT_AREA_05, face_direction=SOUTH, x=27, y=60, z=0
        ),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        SetVarToConst(ACTIVE_NPC, 21),
        RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
        JmpToEvent(E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1753_set_7000_to_7000_short_mem_9",
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 20, ["EVENT_1753_run_event_as_subroutine_3"]
        ),
        JmpIfBitSet(
            TEMP_7044_4,
            ["EVENT_1753_pause_14"],
            identifier="EVENT_1753_jmp_if_bit_set_11",
        ),
        SetVarToConst(ACTIVE_NPC, 22),
        Jmp(["EVENT_1883_jmp_if_bit_set_4"]),
        Pause(1, identifier="EVENT_1753_pause_14"),
        Return(),
        Jmp(["EVENT_1754_run_event_as_subroutine_3"]),
    ]
)
