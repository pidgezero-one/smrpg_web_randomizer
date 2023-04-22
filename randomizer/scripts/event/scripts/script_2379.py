# pylint: disable=C0301

"""E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2379_pause_0"),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_2379_pause_0"]),
        JmpIfMarioInAir(["EVENT_2379_set_bit_5"]),
        ClearBit(TEMP_7044_6),
        Jmp(["EVENT_2379_pause_0"]),
        SetBit(TEMP_7044_6, identifier="EVENT_2379_set_bit_5"),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2379_action_queue_sync_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2379_action_queue_sync_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2379_action_queue_sync_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2379_enter_area_16"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2379_enter_area_16"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2379_enter_area_16"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2379_enter_area_16"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2379_enter_area_16"]),
        Jmp(["EVENT_2379_pause_0"]),
        EnterArea(
            room_id=R238_SMITHY_FACTORY_FALL_FROM_LUGNUT_ROOMS_AREA_06__PRIOR,
            face_direction=NORTHWEST,
            x=15,
            y=10,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_2379_enter_area_16",
        ),
        Return(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetPriority(0),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
            identifier="EVENT_2379_action_queue_sync_18",
        ),
        Jmp(["EVENT_2379_pause_0"]),
    ]
)
