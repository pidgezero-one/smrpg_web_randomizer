# pylint: disable=C0301

"""E2472_BEAN_VALLEY_2ND_PROGRESSION_PIPE_REVERSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 7),
        SetVarToConst(Y_COORD_2, 75),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R252_BEAN_VALLEY_MAIN_AREA,
            face_direction=SOUTH,
            x=13,
            y=66,
            z=0,
            run_entrance_event=True,
        ),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2472_ret_11"]),
        JmpIfBitSet(UNKNOWN_708D_5, ["EVENT_2472_ret_11"]),
        Pause(24),
        ClearBit(SIGNAL_RING_BIT),
        PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
        Return(identifier="EVENT_2472_ret_11"),
    ]
)
