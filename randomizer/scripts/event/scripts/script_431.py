# pylint: disable=C0301

"""E0431_PIPE_VAULT_GOOMBA_THUMPIN_ENTRANCE_PIPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_6),
        SetVarToConst(X_COORD_2, 13),
        SetVarToConst(Y_COORD_2, 38),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R143_PIPE_VAULT_GOOMBATHUMPING_ROOM,
            face_direction=NORTHEAST,
            x=2,
            y=123,
            z=1,
            run_entrance_event=True,
        ),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASTransferXYZFPixels(x=16, y=0, z=0, direction=EAST),
                ASJumpToHeight(height=0, silent=True),
            ],
        ),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_431_pause_8"),
        JmpIfMarioInAir(["EVENT_431_pause_8"]),
        Return(),
    ]
)
