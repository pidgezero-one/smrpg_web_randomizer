# pylint: disable=C0301

"""E1647_MOLEVILLE_MINECART_FREEPLAY_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(PAID_FOR_MINECART, ["EVENT_1647_jmp_if_bit_set_14"]),
        Pause(20),
        PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
                ASPause(8),
            ],
        ),
        RemoveObjectFromCurrentLevel(MARIO),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        Pause(30),
        FadeOutToBlack(sync=False, duration=48),
        EnterArea(
            room_id=R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING,
            face_direction=SOUTH,
            x=19,
            y=27,
            z=12,
        ),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Return(),
        JmpIfBitSet(
            TEMP_7044_3,
            ["EVENT_1647_ret_19"],
            identifier="EVENT_1647_jmp_if_bit_set_14",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASBounceToXYWithHeight(x=20, y=39, height=20), ASFaceWest()],
        ),
        SetSyncActionScript(NPC_2, A0040_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_WATER_DROPLETS),
        RunDialog(
            dialog_id=DI1135_TRY_TO_SNEAK_INTO_MINECART,
            above_object=NPC_2,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(TEMP_7044_3),
        Return(identifier="EVENT_1647_ret_19"),
    ]
)
