# pylint: disable=C0301

"""E0485_PIPE_VAULT_CROUCH_ROOM_ENTRANCE_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(PIPE_VAULT_GATED, ["EVENT_485_set_short_0"]),
        Return(),
        SetVarToConst(X_COORD_2, 17, identifier="EVENT_485_set_short_0"),
        SetVarToConst(Y_COORD_2, 18),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        SetBit(DIRECTIONAL_7049_0),
        EnterArea(
            room_id=R123_PIPE_VAULT_AREA_01,
            face_direction=SOUTH,
            x=2,
            y=26,
            z=1,
            run_entrance_event=True,
        ),
        JmpToEvent(E0282_UNKNOWN_PIPE_VAULT),
    ]
)
