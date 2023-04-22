# pylint: disable=C0301

"""E1188_HENCHMAN_BATTLE_PACK_SELECTOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_1188_room_190_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 325, ["EVENT_1188_room_325_logic"]),
        Return(),
        StartBattleAtBattlefield(
            11, BF28_MUSHROOM_KINGDOM, identifier="EVENT_1188_room_190_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            10, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_1188_room_325_logic"
        ),
        Return(),
    ]
)
