# pylint: disable=C0301

"""E3820_FORCED_TOWER_BOSS_1_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        StartBattleAtBattlefield(161, BF12_BOOSTER_TOWER),
        JmpIfBitClear(GAME_OVER, ["EVENT_3820_remove_from_level_15"]),
        ResetAndChooseGame(),
        RemoveObjectFromSpecificLevel(
            NPC_7,
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            identifier="EVENT_3820_remove_from_level_15"),
        RemoveObjectFromCurrentLevel(NPC_7),
        FadeInFromBlack(sync=False),
        JmpIfBitSet(TOWER_BOSS_1_STAR_PIECE, ["EVENT_3820_ret_20"]),
        SetBit(TOWER_BOSS_1_STAR_PIECE),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_3820_ret_20"),
    ]
)
