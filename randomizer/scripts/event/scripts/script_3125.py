# E3125_SEWER_PIPE_TO_LANDS_END

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 8),
        SetVarToConst(Y_COORD_2, 100),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
            face_direction=SOUTH,
            x=29,
            y=35,
            z=10,
        ),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        JmpToEvent(E1590_SEWER_PIPE_TO_LANDS_END_SUBROUTINE),
    ]
)
