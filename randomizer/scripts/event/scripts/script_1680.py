# pylint: disable=C0301

"""E1680_TEMPLE_PIPE_TO_FORTUNE_RESULT_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 5194),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        SetVarToConst(TEMP_70AC, 0),
        ClearBit(BELOME_HEAD_1),
        ClearBit(BELOME_HEAD_2),
        ClearBit(BELOME_HEAD_3),
        JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1680_enter_area_2"]),
        SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
        EnterArea(
            room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            face_direction=SOUTH,
            x=4,
            y=83,
            z=9,
            identifier="EVENT_1680_enter_area_2",
        ),
        JmpIfBitClear(HAS_A_PRIZE_FORTUNE, ["EVENT_1680_action_queue_sync_6"]),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASJumpToHeight(height=0, silent=True)],
            identifier="EVENT_1680_action_queue_sync_6",
        ),
        JmpToEvent(E1770_TEMPLE_FORTUNE_RESULTS_ROOM_LOADER),
    ]
)
