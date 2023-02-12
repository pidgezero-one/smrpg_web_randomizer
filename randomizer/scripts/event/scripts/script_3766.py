# E3766_BEAN_VALLEY_LOWER_CHEST_ROOM_FALL_TO_HOT_SPRINGS_MEZZANINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH,
            face_direction=SOUTH,
            x=27,
            y=115,
            z=4,
        ),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASJumpToHeight(height=0, silent=True),
            ],
        ),
        FadeInFromBlack(sync=True),
        Pause(24),
        PauseScriptUntilEffectDone(),
        SetBit(TEMP_704A_2),
        EnterArea(
            room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS,
            face_direction=SOUTH,
            x=20,
            y=50,
            z=0,
            run_entrance_event=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=20, y=50, z=0, direction=SOUTHEAST),
                ASVisibilityOn(),
                ASFloatingOn(),
            ],
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3766_action_queue_async_10_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3766_action_queue_async_10_SUBSCRIPT_pause_0"]
                ),
                ASBPL262728(),
                ASJumpToHeight(height=80, silent=True),
            ],
        ),
        SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetWalkingSpeed(NORMAL), ASShiftSouthPixels(8)]
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
