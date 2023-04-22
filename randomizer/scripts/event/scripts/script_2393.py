# pylint: disable=C0301

"""E2393_ABYSS_EXIT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
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
            ],
        ),
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
            ],
        ),
        Pause(24),
        FadeOutToBlack(sync=False, duration=8),
        StopEmbeddedActionScript(MARIO),
        ExitToWorldMap(area=OW05_GATE, bit_6=True, bit_7=True),
        Return(),
    ]
)
