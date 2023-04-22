# pylint: disable=C0301

"""E3614_BELOME_FORTUNE_PRIZE_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 27, ["EVENT_3614_chest_2"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 28, ["EVENT_3614_chest_3"]),
        JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3614_chest_4"]),
        JmpToEvent(E1808_BELOME_FORTUNE_PRIZE_CHEST_1_SUBROUTINE),
        JmpToEvent(E1932_BELOME_FORTUNE_PRIZE_CHEST_2, identifier="EVENT_3614_chest_2"),
        JmpToEvent(E1933_BELOME_FORTUNE_PRIZE_CHEST_3, identifier="EVENT_3614_chest_3"),
        JmpToEvent(E1934_BELOME_FORTUNE_PRIZE_CHEST_4, identifier="EVENT_3614_chest_4"),
    ]
)
