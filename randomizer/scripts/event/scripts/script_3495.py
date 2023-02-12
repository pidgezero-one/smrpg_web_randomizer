# E3495_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ANIMATION_AND_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftSouthwestPixels(8),
                ASFaceSoutheast(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        FadeInFromBlack(sync=True),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["EVENT_3495_run_background_event_2"]),
        RunBackgroundEvent(
            event_id=E3513_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_GRANTER,
            return_on_level_exit=True,
        ),
        RunBackgroundEvent(
            event_id=E3498_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_BACKGROUND,
            return_on_level_exit=True,
            bit_6=True,
            bit_7=True,
            identifier="EVENT_3495_run_background_event_2",
        ),
        FreezeCamera(),
        SetSyncActionScript(MARIO, A0602_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_PLAYER_OUTER),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(160),
                ASSetWalkingSpeed(SLOW),
                ASShiftWestSteps(6),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpToSubroutine(["EVENT_3491_action_queue_sync_16"]),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=14, y=112, z=0
        ),
        FadeOutMusicToVolume(duration=1, volume=56),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=8, y=105),
                ASSetVarToConst(X_COORD_2, 4480),
                ASSetVarToConst(Y_COORD_2, 13696),
                ASTransferTo70167018(),
            ],
        ),
        JmpToSubroutine(["EVENT_3480_action_queue_async_73"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x80\x02\xec\xff")),
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthwestSteps(2),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
        Jmp(["EVENT_3489_enable_controls_3"]),
        Return(),
    ]
)
