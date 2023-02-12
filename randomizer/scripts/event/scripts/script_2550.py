# E2550_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_GECKIT_RUNS_AT_YOU

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            ["EVENT_2550_ret_3"],
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM
        ),
        SetSyncActionScript(NPC_2, A0852_VALLEY_RIGHT_PIPE_2ND_GECKO_RUNNING),
        Return(identifier="EVENT_2550_ret_3"),
    ]
)
