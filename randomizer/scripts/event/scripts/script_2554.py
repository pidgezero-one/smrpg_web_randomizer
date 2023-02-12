# E2554_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_STAIRCASE_ITEM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BEAN_VALLEY_BIG_PIPE_ROOM_INVISIBLE_ITEM, ["EVENT_2554_ret_6"]),
        SetBit(BEAN_VALLEY_BIG_PIPE_ROOM_INVISIBLE_ITEM),
        RemoveObjectFromSpecificLevel(
            NPC_9, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM
        ),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(identifier="EVENT_2554_ret_6"),
    ]
)
