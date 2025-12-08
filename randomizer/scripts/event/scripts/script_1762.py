# pylint: disable=C0301

"""E1762_LANDS_END_STAGE_2_WHIRLPOOL_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R404_LANDS_END_DESERT_AREA_04,
            ["EVENT_1762_run_event_as_subroutine_3"]),
        SetVarToConst(ACTIVE_NPC, 23),
        Jmp(["EVENT_1886_jmp_if_bit_set_4"]),
        RunEventAsSubroutine(
            E1544_SAND_WHIRLPOOL, identifier="EVENT_1762_run_event_as_subroutine_3"
        ),
        EnterArea(
            room_id=R403_LANDS_END_DESERT_AREA_05, face_direction=SOUTH, x=27, y=60, z=0
        ),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        SetVarToConst(ACTIVE_NPC, 20),
        RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
        JmpToEvent(E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE),
    ]
)
