# pylint: disable=C0301

"""E3492_MIDAS_RIVER_MID_LEFT_TUNNEL_ANIMATION_AND_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=True),
        FreezeCamera(),
        SetSyncActionScript(MARIO, A0599_MIDAS_RIVER_MID_LEFT_TUNNEL_PLAYER_OUTER),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASWalkEastSteps(2),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkEastSteps(2),
                ASSetWalkingSpeed(SLOW),
                ASWalkEastSteps(6),
                ASSetWalkingSpeed(NORMAL),
                ASWalkEastSteps(5),
                ASWalkSoutheastSteps(3),
                ASSetWalkingSpeed(SLOW),
                ASWalkSoutheastSteps(5),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepSoutheast(),
                ASWalkEastSteps(5),
                ASSetWalkingSpeed(SLOW),
                ASWalkEastSteps(1),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpToSubroutine(["EVENT_3491_action_queue_sync_16"]),
        JmpIfBitClear(TEMP_7043_4, ["EVENT_3492_enter_area_8"]),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL,
            face_direction=SOUTH,
            x=6,
            y=56,
            z=0,
            identifier="EVENT_3492_enter_area_8",
        ),
        FadeOutMusicToVolume(duration=1, volume=56),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=13, y=67),
                ASSetVarToConst(X_COORD_2, 7040),
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
                ASWalkSouthPixels(32),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x80\x02\xf4\xff")),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASWalkNorthwestSteps(7),
                ASWalkSouthwestPixels(4),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
        Jmp(["EVENT_3489_enable_controls_3"]),
        Return(),
    ]
)
