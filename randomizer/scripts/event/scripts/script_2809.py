# E2809_MUSHROOM_WAY_BOSS_THREATENS_YOU

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TEMP_7044_6, "script_2809_jmp_if_mem_set", identifier="script_2809_begin"
        ),
        Pause(1),
        Jmp("script_2809_begin"),
        JmpIfBitSet(
            TOAD_IN_MUSHROOM_WAY_3,
            "script_2809_end",
            identifier="script_2809_jmp_if_mem_set",
        ),
        ClearBit(TEMP_7044_6),
        FreezeAllNPCsUntilReturn(),
        EnableControls([]),
        ActionQueueAsync(MARIO, [FaceNortheast(), Pause(16)]),
        ActionQueueAsync(SCREEN_FOCUS, [SetWalkingSpeed(FAST), WalkToXYCoords(24, 80)]),
        FreezeCamera(),
        ActionQueueAsync(
            NPC_7,
            [
                SequenceLoopingOn(),
                SetSequenceSpeed(FAST),
                Pause(40),
                SetSequenceSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            MARIO,
            [
                Pause(5),
                FixedFCoordOn(),
                SetWalkingSpeed(SLOW),
                ShiftSouthwestSteps(1),
                SetWalkingSpeed(NORMAL),
                FixedFCoordOff(),
            ],
        ),
        Pause(10),
        UnfreezeAllNPCs(),
        EnableControls(LEFT, RIGHT, DOWN, UP, X, A, Y, B),
        UnfreezeCamera(),
        Return(identifier="script_2809_end"),
    ]
)
