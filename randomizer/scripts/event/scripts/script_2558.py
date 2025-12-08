# pylint: disable=C0301

"""E2558_BEAN_VALLEY_BOSS_ROOM_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(BEAN_VALLEY_BOSS_DEFEATED, ["EVENT_2558_ret_6"]),
        SetVarToConst(X_COORD_2, 27),
        SetVarToConst(Y_COORD_2, 70),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA,
            face_direction=SOUTH,
            x=26,
            y=22,
            z=0,
            run_entrance_event=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        Return(identifier="EVENT_2558_ret_6"),
    ]
)
