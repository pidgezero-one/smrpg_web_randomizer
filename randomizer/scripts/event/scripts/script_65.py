# pylint: disable=C0301

"""E0065_TRAMPOLINE_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseScriptIfMenuOpen(),
        JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_65_action_queue_sync_6"]),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(NORMAL),
                ASPause(36),
                ASSetSequenceSpeed(FAST),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(3),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownPixels(1),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(4),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftZDownPixels(2),
                ASPause(2),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(1),
                ASPause(9),
                ASSetWalkingSpeed(NORMAL),
                ASSequencePlaybackOn(),
                ASJumpToHeight(height=256, silent=True),
                ASFloatingOn(),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        Pause(6),
        Return(),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(24),
                ASSetSequenceSpeed(NORMAL),
                ASResetProperties(),
                ASSequenceLoopingOff(),
            ],
            identifier="EVENT_65_action_queue_sync_6",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(1),
                ASSetWalkingSpeed(FAST),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASShiftZDownPixels(14),
                ASPause(8),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=108, silent=True),
                ASFloatingOn(),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
                ASWalk1StepSouth(),
                ASSetSolidityBits(cant_pass_npcs=True),
            ],
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        RememberLastObject(),
        ClearBit(DIRECTIONAL_7049_0),
        MoveScriptToMainThread(),
        EndAll(),
    ]
)
