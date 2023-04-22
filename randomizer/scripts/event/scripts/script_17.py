# pylint: disable=C0301

"""E0017_FIGHT_REMOVE_TEMPORARILY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_17_disable_trigger_2"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_17_disable_trigger_2"),
        ClearBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        StartBattleWithPackAt700E(),
        JmpToEvent(E0024_BATTLE_RESULT_CHECK),
    ]
)
