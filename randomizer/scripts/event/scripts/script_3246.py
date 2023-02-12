# E3246_DRY_BONES_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 169, ["EVENT_3246_start_battle_5"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 182, ["EVENT_3246_start_battle_5"]),
        StartBattleAtBattlefield(72, BF04_SUNKEN_SHIP),
        Jmp(["EVENT_3246_jmp_if_bit_set_6"]),
        StartBattleAtBattlefield(
            73, BF04_SUNKEN_SHIP, identifier="EVENT_3246_start_battle_5"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_3246_set_temp_action_script_sync_12"],
            identifier="EVENT_3246_jmp_if_bit_set_6",
        ),
        JmpIfBitSet(GAME_OVER, ["EVENT_3246_reset_and_choose_game_15"]),
        SetTempSyncActionScript(MEM_70A8, A0920_STATIC_DRY_BONES_COLLAPSE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASShiftZDownPixels(2),
                ASResetProperties(),
                ASSetSolidityBits(cant_pass_npcs=True),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            MEM_70A8,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_3246_set_temp_action_script_sync_12",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_3246_reset_and_choose_game_15"),
    ]
)
