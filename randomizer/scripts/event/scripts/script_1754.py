# pylint: disable=C0301

"""E1754_LANDS_END_FINAL_WHIRLPOOL_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AC, 0),
        ClearBit(BELOME_HEAD_1),
        ClearBit(BELOME_HEAD_2),
        ClearBit(BELOME_HEAD_3),
        JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1754_jmp_if_object_in_level_0"]),
        SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R319_LANDS_END_DESERT_AREA_06,
            ["EVENT_1754_set_7000_to_7000_short_mem_11"],
            identifier="EVENT_1754_jmp_if_object_in_level_0"),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 21, ["EVENT_1753_run_event_as_subroutine_3"]
        ),
        RunEventAsSubroutine(
            E1544_SAND_WHIRLPOOL, identifier="EVENT_1754_run_event_as_subroutine_3"
        ),
        EnterArea(
            room_id=R263_LANDS_END_UNDERGROUND_AREA_01,
            face_direction=SOUTH,
            x=5,
            y=91,
            z=15,
            run_entrance_event=True),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        JmpIfBitClear(LANDS_END_CHEST_2_REQUESTED, ["EVENT_1754_ret_10"]),
        SummonObjectToSpecificLevel(
            NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        Return(identifier="EVENT_1754_ret_10"),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1754_set_7000_to_7000_short_mem_11"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_1753_jmp_if_bit_set_11"]),
        Jmp(["EVENT_1753_run_event_as_subroutine_3"]),
        Jmp(["EVENT_1753_run_event_as_subroutine_3"]),
    ]
)
