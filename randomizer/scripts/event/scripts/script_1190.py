# pylint: disable=C0301

"""E1190_HENCHMAN_BATTLE_PACK_SELECTOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_1190_room_190_logic"]),
        Return(),
        StartBattleAtBattlefield(
            11, BF28_MUSHROOM_KINGDOM, identifier="EVENT_1190_room_190_logic"
        ),
        Return(),
    ]
)
