# pylint: disable=C0301

"""E2487_BEAN_VALLEY_RIGHTMOST_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_2487_ret_5"]
        ),
        SetVarToConst(X_COORD_2, 10),
        SetVarToConst(Y_COORD_2, 29),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            face_direction=SOUTH,
            x=8,
            y=112,
            z=0,
            run_entrance_event=True),
        Return(identifier="EVENT_2487_ret_5"),
    ]
)
