# pylint: disable=C0301

"""E1824_KEEP_SET_PLATFORM_PROPERTIES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        Pause(1),
        SetVarToConst(TEMP_70A9, 22),
        SetVarToConst(PRIMARY_TEMP_700C, 2),
        StartLoopNTimes(5),
        ActionQueueAsync(
            target=MEM_70A9,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFaceNortheast(),
                ASWalkFDirection16Pixels(),
                ASSetWalkingSpeed(SLOW),
            ],
        ),
        Inc(TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_700C, 2),
        EndLoop(),
        UnfreezeAllNPCs(),
        SetVarToConst(ROSE_WAY_7038, 2176),
        SetVarToConst(ROSE_WAY_703A, 7296),
        SetVarToConst(ROSE_WAY_703C, 1280),
        RunBackgroundEvent(
            event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1824_jmp_to_event_17"]),
        ClearBit(TEMP_7095_4),
        JmpToEvent(
            E1829_KEEP_DISPLAY_REMAINING_TRIES, identifier="EVENT_1824_jmp_to_event_17"
        ),
    ]
)
