# pylint: disable=C0301

"""E1310_TOWER_CHECKERBOARD_COLLECT_KEY_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromSpecificLevel(
            NPC_5,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
    ]
)
