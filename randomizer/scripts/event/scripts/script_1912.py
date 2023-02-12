# E1912_ABYSS_MACHINE_ARROW_HIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([]),
        SetBit(TEMP_7043_1),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(128),
                ASSetWalkingSpeed(FAST),
                ASShiftSoutheastSteps(2),
                ASVisibilityOff(),
                ASClearBit(TEMP_7043_0),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(3),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO012_DIZZINESS, channel=4),
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(
                    index=15, sprite_offset=1, is_sequence=True, looping=True
                ),
            ],
        ),
        SetVarToConst(TIMER_701C, 90),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1914_ABYSS_MACHINE_ARROW_RESET, timer_var=TIMER_701C
        ),
        Return(),
    ]
)
