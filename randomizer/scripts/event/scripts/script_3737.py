# E3737_NIMBUS_CASTLE_BACK_EXIT_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3585_fade_in_from_black_async_0"]),
        SetBit(NIMBUS_BOSS_IN_TOWN_SQUARE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=15, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(1),
                ASResetProperties(),
                ASShadowOff(),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalk1StepEast()],
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASSequenceLoopingOn(),
                ASPause(60),
                ASSetSequenceSpeed(NORMAL),
                ASPause(30),
                ASSetSequenceSpeed(SLOW),
                ASPause(10),
                ASSequenceLoopingOff(),
                ASPause(60),
                ASSetSpriteSequence(
                    index=15, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=15, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASSetWalkingSpeed(FAST),
                ASStartLoopNTimes(2),
                ASShiftSouthwestPixels(4),
                ASPause(3),
                ASShiftNortheastPixels(4),
                ASEndLoop(),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(60),
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASFloatingOn(),
            ],
        ),
        Pause(10),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST,
            face_direction=NORTHEAST,
            x=27,
            y=29,
            z=6,
        ),
        RunEventAtReturn(E3745_NIMBUS_BACK_EXIT_INITIATE_FALLING_SEQUENCE),
        Return(),
    ]
)
