# pylint: disable=C0301

"""E1675_MARIO_BUMPED_OFF_CANNON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x90")),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASFloatingOff(),
                ASRunAwayShift(),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(height=96, silent=True),
                ASFloatingOn(),
                ASSetSpriteSequence(
                    index=7, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPause(1),
            ],
        ),
        ResumeActionScript(MEM_70A8),
        MoveScriptToBackgroundThread2(),
        ActionQueueAsync(target=MARIO, subscript=[ASWalkNorthwestSteps(5)]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastPixels(4),
                ASWalkNorthwestPixels(8),
                ASWalkSoutheastPixels(8),
                ASWalkNorthwestPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASJumpToHeight(height=80, silent=True),
                ASWalk1StepSouth(),
                ASSetAllSpeeds(NORMAL),
                ASSetSpriteSequence(
                    index=7, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(60),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(1, identifier="EVENT_1675_pause_7"),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_1675_action_queue_sync_11"]),
        Jmp(["EVENT_1675_pause_7"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASResetProperties(), ASFaceSouth(), ASJumpToHeight(108)],
            identifier="EVENT_1675_action_queue_sync_11",
        ),
        MoveScriptToMainThread(),
        Return(),
    ]
)
