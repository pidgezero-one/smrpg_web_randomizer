# pylint: disable=C0301

"""E1582_LANDS_END_TRAMPOLINE_TO_SEWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            SEWERS_FLIPPED_CHEST_OPENED, ["EVENT_1582_run_event_as_subroutine_4"]
        ),
        JmpIfBitClear(TEMP_7044_0, ["EVENT_1582_run_event_as_subroutine_4"]),
        SetBit(TEMP_7042_2),
        EnableObjectTriggerInSpecificLevel(
            NPC_1, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS
        ),
        RunEventAsSubroutine(
            E0065_TRAMPOLINE_SUBROUTINE,
            identifier="EVENT_1582_run_event_as_subroutine_4",
        ),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            face_direction=SOUTH,
            x=8,
            y=100,
            z=14,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(),
    ]
)
