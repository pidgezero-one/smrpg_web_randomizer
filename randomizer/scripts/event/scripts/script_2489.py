# E2489_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftZUpSteps(11),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_2489_action_queue_async_11_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2489_action_queue_async_11_SUBSCRIPT_pause_1"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
