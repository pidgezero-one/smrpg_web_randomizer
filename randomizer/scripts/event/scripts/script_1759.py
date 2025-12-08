# pylint: disable=C0301

"""E1759_LANDS_END_PENULTIMATE_WHIRLPOOL_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R403_LANDS_END_DESERT_AREA_05,
            ["EVENT_1759_set_7000_to_7000_short_mem_9"]),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 21, ["EVENT_1758_run_event_as_subroutine_3"]
        ),
        RunEventAsSubroutine(
            E1544_SAND_WHIRLPOOL, identifier="EVENT_1759_run_event_as_subroutine_3"
        ),
        EnterArea(
            room_id=R404_LANDS_END_DESERT_AREA_04,
            face_direction=SOUTH,
            x=22,
            y=102,
            z=0),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        SetVarToConst(ACTIVE_NPC, 22),
        RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
        JmpToEvent(E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1759_set_7000_to_7000_short_mem_9"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_1758_jmp_if_bit_set_11"]),
        Jmp(["EVENT_1759_run_event_as_subroutine_3"]),
        Jmp(["EVENT_1758_run_event_as_subroutine_3"]),
    ]
)
