# E3336_CORKPEDITE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 363, ["EVENT_3336_jmp_if_object_not_in_level_7"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 362, ["EVENT_3336_jmp_if_object_not_in_level_9"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE,
            ["EVENT_3336_run_event_as_subroutine_12"],
            identifier="EVENT_3336_jmp_if_object_not_in_level_7",
        ),
        Jmp(["EVENT_3336_action_queue_async_10"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE,
            ["EVENT_3336_run_event_as_subroutine_12"],
            identifier="EVENT_3336_jmp_if_object_not_in_level_9",
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthwestPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3336_action_queue_async_10",
        ),
        RunBackgroundEvent(
            event_id=E3337_CORKPEDITE_ANIMATION, return_on_level_exit=True
        ),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER,
            identifier="EVENT_3336_run_event_as_subroutine_12",
        ),
        Return(),
    ]
)
