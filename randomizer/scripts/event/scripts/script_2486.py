# pylint: disable=C0301

"""E2486_BEAN_VALLEY_BOTTOM_LEFT_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_2486_ret_5"]
        ),
        SetVarToConst(X_COORD_2, 7),
        SetVarToConst(Y_COORD_2, 34),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT,
            face_direction=SOUTH,
            x=24,
            y=102,
            z=2,
            run_entrance_event=True),
        Return(identifier="EVENT_2486_ret_5"),
    ]
)
