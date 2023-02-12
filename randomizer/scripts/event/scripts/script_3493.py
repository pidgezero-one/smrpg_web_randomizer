# E3493_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            MIDAS_RIVER_TUNNEL_2_BIT_2, ["EVENT_3493_fade_in_from_black_sync_2"]
        ),
        RunBackgroundEvent(
            event_id=E3496_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT_BACKGROUND,
            return_on_level_exit=True,
        ),
        FadeInFromBlack(sync=True, identifier="EVENT_3493_fade_in_from_black_sync_2"),
        FreezeCamera(),
        SetSyncActionScript(MARIO, A0600_MIDAS_RIVER_MID_RIGHT_TUNNEL_PLAYER_OUTER),
        SetSyncActionScript(SCREEN_FOCUS, A0647_MIDAS_MID_RIGHT_TUNNEL_CAMERA),
        JmpToSubroutine(["EVENT_3491_action_queue_sync_16"]),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=56, z=0
        ),
        FadeOutMusicToVolume(duration=1, volume=56),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=12, y=67),
                ASSetVarToConst(X_COORD_2, 6528),
                ASSetVarToConst(Y_COORD_2, 8320),
                ASTransferTo70167018(),
            ],
        ),
        JmpToSubroutine(["EVENT_3480_action_queue_async_73"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthPixels(32),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x80\x02\xf2\xff")),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASShiftNorthwestSteps(6),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
        Jmp(["EVENT_3489_enable_controls_3"]),
        Return(),
    ]
)
