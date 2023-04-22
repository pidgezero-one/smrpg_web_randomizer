# pylint: disable=C0301

"""E0708_MARRYMORE_TIP_DECISION_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_708_prize_1"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_708_prize_2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_708_prize_3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_708_prize_4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_708_prize_5"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 200, ["EVENT_708_prize_6"]),
        Return(),
        JmpToEvent(E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_708_prize_1"),
        Return(),
        JmpToEvent(E0179_NPC_QUEST_2_CONTAINER, identifier="EVENT_708_prize_2"),
        Return(),
        JmpToEvent(E0180_NPC_QUEST_3_CONTAINER, identifier="EVENT_708_prize_3"),
        Return(),
        JmpToEvent(E0181_NPC_QUEST_4_CONTAINER, identifier="EVENT_708_prize_4"),
        Return(),
        JmpToEvent(E0182_NPC_QUEST_5_CONTAINER, identifier="EVENT_708_prize_5"),
        Return(),
        JmpToEvent(E0183_NPC_QUEST_6_CONTAINER, identifier="EVENT_708_prize_6"),
        Return(),
    ]
)
