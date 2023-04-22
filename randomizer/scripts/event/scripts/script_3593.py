# pylint: disable=C0301

"""E3593_GET_ITEM_FROM_CHAPEL_HENCHMAN_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_3593_pause_22"]),
        FreezeAllNPCsUntilReturn(),
        JmpIfBitSet(CHAPEL_ITEM_3_RETRIEVED, ["EVENT_3593_jmp_to_subroutine_10"]),
        SetVarToConst(PRIMARY_TEMP_7000, 2),
        RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
        UnfreezeAllNPCs(),
        SetBit(CHAPEL_ITEM_3_RETRIEVED),
        Return(),
        JmpToSubroutine(
            ["EVENT_3593_pause_22"], identifier="EVENT_3593_jmp_to_subroutine_10"
        ),
        FreezeAllNPCsUntilReturn(),
        SetVarToConst(PRIMARY_TEMP_7000, 2),
        RunDialog(
            dialog_id=DI2496_WHERES_THE_CROWN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        Pause(1, identifier="EVENT_3593_pause_22"),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_3593_pause_22"]),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_3593_pause_22"]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_3593_pause_22"]),
        Return(),
    ]
)
