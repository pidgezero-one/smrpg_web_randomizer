# pylint: disable=C0301

"""E0487_PIPE_VAULT_CHOMPWEED_ROOM_EXIT_PIPE_REVERSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 5),
        SetVarToConst(Y_COORD_2, 20),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
            face_direction=SOUTHWEST,
            x=26,
            y=56,
            z=2,
            run_entrance_event=True,
        ),
        RunEventAsSubroutine(E0269_PIPE_UP_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_487_ret_26"]),
        RunEventAsSubroutine(E3900_PIPE_VAULT_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_487_ret_26"),
    ]
)
