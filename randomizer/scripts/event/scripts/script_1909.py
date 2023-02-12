# E1909_ABYSS_CONVEYOR_BELT_JABIT_OR_BOWYER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        JmpIfRandom1of2(["EVENT_1909_set_short_4"]),
        SetVarToConst(BATTLE_PACK_ID, 136),
        Jmp(["EVENT_1909_start_battle_700E_5"]),
        SetVarToConst(BATTLE_PACK_ID, 137, identifier="EVENT_1909_set_short_4"),
        StartBattleWithPackAt700E(identifier="EVENT_1909_start_battle_700E_5"),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1909_disable_trigger_10"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
        ActionQueueAsync(target=MEM_70A8, subscript=[ASVisibilityOff()]),
        SetBit(UNKNOWN_704D_0),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_1909_disable_trigger_10"),
        ResumeActionScript(MEM_70A8),
        UnfreezeAllNPCs(),
        FadeInFromBlack(sync=False),
        SetVarToConst(TIMER_701C, 2),
        Return(),
    ]
)
