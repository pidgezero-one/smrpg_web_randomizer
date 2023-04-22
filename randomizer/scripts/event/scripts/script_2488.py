# pylint: disable=C0301

"""E2488_BEAN_VALLEY_BOTTOM_RIGHT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_2488_ret_5"]
        ),
        SetVarToConst(X_COORD_2, 9),
        SetVarToConst(Y_COORD_2, 35),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT,
            face_direction=SOUTH,
            x=16,
            y=56,
            z=0,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_2488_ret_5"),
    ]
)
