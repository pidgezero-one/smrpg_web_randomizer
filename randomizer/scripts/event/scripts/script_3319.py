# pylint: disable=C0301

"""E3319_SET_VOMER_PACK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_3319_set_7000_to_current_level_2"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        Set7000ToCurrentLevel(identifier="EVENT_3319_set_7000_to_current_level_2"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 367, ["EVENT_3319_start_battle_7"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 364, ["EVENT_3319_start_battle_7"]),
        StartBattleAtBattlefield(108, BF20_BARREL_VOLCANO),
        Jmp(["EVENT_3319_jmp_if_bit_set_8"]),
        StartBattleAtBattlefield(
            109, BF20_BARREL_VOLCANO, identifier="EVENT_3319_start_battle_7"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_3319_set_temp_action_script_sync_14"],
            identifier="EVENT_3319_jmp_if_bit_set_8"),
        JmpIfBitSet(GAME_OVER, ["EVENT_3319_reset_and_choose_game_17"]),
        SetTempSyncActionScript(MEM_70A8, A0273_VOLCANO_DRY_BONES_COLLAPSE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASShiftZDownPixels(2),
                ASResetProperties(),
                ASSetSolidityBits(cant_pass_npcs=True),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
        SetTempSyncActionScript(
            MEM_70A8,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_3319_set_temp_action_script_sync_14"),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_3319_reset_and_choose_game_17"),
    ]
)
