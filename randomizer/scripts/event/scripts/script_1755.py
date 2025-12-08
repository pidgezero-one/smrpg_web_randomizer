# pylint: disable=C0301

"""E1755_LANDS_END_SHY_AWAY_WHIRLPOOL_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R402_LANDS_END_DESERT_AREA_03,
            ["EVENT_1755_run_event_as_subroutine_3"]),
        SetVarToConst(ACTIVE_NPC, 26),
        Jmp(["EVENT_1884_jmp_if_bit_set_4"]),
        RunEventAsSubroutine(
            E1544_SAND_WHIRLPOOL, identifier="EVENT_1755_run_event_as_subroutine_3"
        ),
        EnterArea(
            room_id=R404_LANDS_END_DESERT_AREA_04,
            face_direction=SOUTH,
            x=22,
            y=102,
            z=0),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        SetVarToConst(ACTIVE_NPC, 20),
        RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
        JmpToEvent(E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE),
    ]
)
