# pylint: disable=C0301

"""E1905_ABYSS_EXIT_TO_BOSS_2_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(ABYSS_BOSS_2_DEFEATED, ["EVENT_1905_enter_area_9"]),
        RemoveObjectFromCurrentLevel(MARIO),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        Pause(50),
        FadeOutToBlack(sync=True, duration=180),
        PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASStartLoopNTimes(59),
                ASWalkEastPixels(8),
                ASWalkWestPixels(8),
                ASEndLoop(),
            ],
        ),
        EnterArea(
            room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM,
            face_direction=SOUTH,
            x=23,
            y=54,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        EnterArea(
            room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM,
            face_direction=SOUTH,
            x=23,
            y=54,
            z=0,
            identifier="EVENT_1905_enter_area_9",
        ),
        FadeInFromBlack(sync=True),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=24, y=54, z=18, direction=EAST),
                ASJumpToHeight(height=0, silent=True),
            ],
        ),
        Return(),
    ]
)
