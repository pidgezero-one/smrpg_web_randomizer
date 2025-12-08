# pylint: disable=C0301

"""E1845_CLOUD_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1845_disable_trigger_2"]),
        RunEventAsSubroutine(E0255_EXP_STAR_HIT),
        Jmp(["EVENT_1845_jmp_if_already_got_star_piece"]),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_1845_disable_trigger_2"),
        ClearBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        SetVarToConst(PRIMARY_TEMP_7000, 519),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfBitSet(
            LANDS_END_CLOUD_STAR_PIECE,
            ["EVENT_1845_ret"],
            identifier="EVENT_1845_jmp_if_already_got_star_piece"),
        SetBit(LANDS_END_CLOUD_STAR_PIECE),
        SetVarToConst(PRIMARY_TEMP_7000, 519),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(identifier="EVENT_1845_ret"),
    ]
)
