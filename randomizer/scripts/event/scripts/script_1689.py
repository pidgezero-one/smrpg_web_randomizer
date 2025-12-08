# pylint: disable=C0301

"""E1689_TEMPLE_PIPE_TO_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 7440),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            face_direction=SOUTH,
            x=4,
            y=43,
            z=9),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        JmpToEvent(E1771_TEMPLE_BOSS_ROOM_LOADER),
    ]
)
