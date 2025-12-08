# pylint: disable=C0301

"""E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(UNKNOWN_704D_1),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1827_set_short_3"]),
        ClearBit(TEMP_7095_4),
        SetVarToConst(ROSE_WAY_7038, 3712, identifier="EVENT_1827_set_short_3"),
        SetVarToConst(ROSE_WAY_703A, 14976),
        SetVarToConst(ROSE_WAY_703C, 512),
        SetVarToConst(TEMP_70A9, 21),
        StartLoopNTimes(8),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASShiftZUpPixels(4),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ]),
        Inc(TEMP_70A9),
        EndLoop(),
        StartLoopNTimes(3),
        ActionQueueSync(target=MEM_70A9, subscript=[ASShiftZUpPixels(4)]),
        Inc(TEMP_70A9),
        EndLoop(),
        SetVarToConst(TEMP_70A9, 21),
        StartLoopNTimes(8),
        SetSyncActionScript(MEM_70A9, A0829_KEEP_XY_PLATFORMS),
        Inc(TEMP_70A9),
        EndLoop(),
        RemoveObjectFromCurrentLevel(NPC_9),
        RunBackgroundEvent(
            event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True
        ),
        RunBackgroundEvent(
            event_id=E1833_KEEP_LINEAR_PLATFORM_ROOM_BACKGROUND,
            return_on_level_exit=True,
            bit_6=True),
        JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES),
    ]
)
