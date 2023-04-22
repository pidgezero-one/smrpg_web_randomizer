# pylint: disable=C0301

"""E0018_FIGHT_DO_NOT_REMOVE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_18_disable_trigger_2"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_18_disable_trigger_2"),
        ClearBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        JmpToEvent(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
    ]
)
