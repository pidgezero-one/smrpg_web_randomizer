# E3206_SEA_PIPE_TO_SHIP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 4),
        SetVarToConst(Y_COORD_2, 38),
        SetBit(MAP_SUNKEN_SHIP),
        SetBit(MAP_DIRECTIONAL_SEA_SUNKEN_SHIP),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R160_SUNKEN_SHIP_AREA_01,
            face_direction=SOUTH,
            x=4,
            y=18,
            z=8,
            run_entrance_event=True,
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceSouth(), ASJumpToHeight(height=0, silent=True)],
        ),
        Return(),
    ]
)
