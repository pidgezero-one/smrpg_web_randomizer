# E1717_BANDITS_WAY_4_MANAGE_DOG_COLLISION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1717_set_short_3"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        SetVarToConst(BATTLE_PACK_ID, 9, identifier="EVENT_1717_set_short_3"),
        StartBattleWithPackAt700E(),
        ClearBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        ActionQueueSync(
            target=MARIO, subscript=[ASPause(1), ASJumpToHeight(height=0, silent=True)]
        ),
        SetVarToConst(TEMP_70AB, 22),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        UnfreezeAllNPCs(),
        Return(),
    ]
)
