# pylint: disable=C0301

"""E1669_NIMBUS_FINAL_HALLWAY_MINIBOSS_COLLISION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1669_set_short_3"]),
        SetBit(DODO_PRESENT_IN_NIMBUS_HALL),
        JmpToEvent(E0255_EXP_STAR_HIT),
        SetVarToConst(PRIMARY_TEMP_7000, 520, identifier="EVENT_1669_set_short_3"),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
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
        JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_1669_ret_14"]),
        SetBit(STATUE_KEEPER_STAR_PIECE),
        SetVarToConst(PRIMARY_TEMP_7000, 520),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(identifier="EVENT_1669_ret_14"),
    ]
)
