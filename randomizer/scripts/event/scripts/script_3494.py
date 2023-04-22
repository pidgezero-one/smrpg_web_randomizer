# pylint: disable=C0301

"""E3494_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ANIMATION_AND_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunBackgroundEvent(
            event_id=E3497_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ITEM_GRANTER,
            return_on_level_exit=True,
        ),
        FadeInFromBlack(sync=True),
        FreezeCamera(),
        SetSyncActionScript(MARIO, A0601_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_PLAYER_OUTER),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(220),
                ASSetWalkingSpeed(NORMAL),
                ASWalkWestSteps(4),
                ASSetWalkingSpeed(NORMAL),
                ASWalkNorthwestSteps(7),
                ASWalk1StepNorthwest(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        MoveScriptToBackgroundThread2(),
        JmpToSubroutine(["EVENT_3491_action_queue_sync_16"]),
        MoveScriptToMainThread(),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=4, y=83, z=0
        ),
        FadeOutMusicToVolume(duration=1, volume=56),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=4, y=76),
                ASSetVarToConst(X_COORD_2, 1408),
                ASSetVarToConst(Y_COORD_2, 8576),
                ASTransferTo70167018(),
            ],
        ),
        JmpToSubroutine(["EVENT_3480_action_queue_async_73"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(8),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x80\x02\xe4\xff")),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASWalkSoutheastSteps(3),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
        Jmp(["EVENT_3489_enable_controls_3"]),
        Return(),
    ]
)
