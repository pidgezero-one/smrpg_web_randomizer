# E3605_PIPE_VAULT_PIPE_TO_TRIPLE_CHEST_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_3),
        SetVarToConst(X_COORD_2, 7),
        SetVarToConst(Y_COORD_2, 50),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            face_direction=NORTHEAST,
            x=0,
            y=79,
            z=0,
            run_entrance_event=True,
        ),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASJumpToHeight(height=0, silent=True),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
