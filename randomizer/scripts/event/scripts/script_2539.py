# pylint: disable=C0301

"""E2539_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7047_0),
        ActionQueueSync(
            target=MEM_70A8, subscript=[ASSetSpriteSequence(index=0, looping=False)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
                ASShadowOff(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkSouthPixels(8),
            ]),
        SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
        PlaySound(sound=SO010_TRAMPOLINE, channel=6),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(4),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x0f\xf0\xff")),
                ASPause(48),
                ASBPL262728(),
            ]),
        Pause(24),
        FadeOutToBlack(sync=False, duration=8),
        StopEmbeddedActionScript(MARIO),
        EnterArea(
            room_id=R251_BEAN_VALLEY_PIRANHA_PIPE_AREA,
            face_direction=SOUTH,
            x=5,
            y=29,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
