# pylint: disable=C0301

"""E2292_ENDING_CREDITS_TOADOFSKY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R441_ENDING_CREDITS_TOADOFSKY_CONDUCTS_CHOIR,
            face_direction=NORTHEAST,
            x=3,
            y=17,
            z=0),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASBounceToXYWithHeight(x=0, y=2, height=0),
            ]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_2, subscript=[ASWalkNorthPixels(3)]),
        Set0158Bit7Offset(0x0158),
        StarMaskExpandFromScreenCenter(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASWalkSouthwestPixels(8),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(15),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPause(45),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(50),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ]),
        SetSyncActionScript(NPC_2, A1015_END_CREDITS_FROGFUCIUS_RAISES),
        Pause(30),
        Clear0158Bit7Offset(0x0158),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPause(80),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(145),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPause(120),
                ASSetWalkingSpeed(VERY_SLOW),
                ASStartLoopNTimes(30),
                ASWalkNorthPixels(1),
                ASPause(4),
                ASEndLoop(),
            ]),
        Pause(60),
        StarMaskShrinkToScreenCenter(),
        Pause(60),
        JmpToEvent(E3801_ENDING_CREDITS_RED_STAR),
        Return(),
    ]
)
