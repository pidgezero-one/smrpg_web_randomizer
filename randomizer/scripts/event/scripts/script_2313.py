# pylint: disable=C0301

"""E2313_BOOSTER_PASS_ARTICHOKER_ENCOUNTER_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(NPC_6),
        RemoveObjectFromSpecificLevel(NPC_6, R100_BOOSTER_PASS_AREA_01),
        StartBattleAtBattlefield(139, BF10_MOUNTAINS),
        JmpIfBitClear(GAME_OVER, ["EVENT_2313_remove_from_current_level_5"]),
        ResetAndChooseGame(),
        RemoveObjectFromCurrentLevel(
            NPC_6, identifier="EVENT_2313_remove_from_current_level_5"
        ),
        Store01To0248(),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=3
        ),
        Store00To0248(),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
