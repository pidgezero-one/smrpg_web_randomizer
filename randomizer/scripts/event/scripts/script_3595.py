# pylint: disable=C0301

"""E3595_GET_ITEM_FROM_CHAPEL_HENCHMAN_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_3593_pause_22"]),
        FreezeAllNPCsUntilReturn(),
        JmpIfBitSet(CHAPEL_ITEM_1_RETRIEVED, ["EVENT_3595_jmp_to_subroutine_10"]),
        SetVarToConst(PRIMARY_TEMP_7000, 3),
        RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
        UnfreezeAllNPCs(),
        SetBit(CHAPEL_ITEM_1_RETRIEVED),
        Return(),
        JmpToSubroutine(
            ["EVENT_3593_pause_22"], identifier="EVENT_3595_jmp_to_subroutine_10"
        ),
        FreezeAllNPCsUntilReturn(),
        SetVarToConst(PRIMARY_TEMP_7000, 3),
        RunDialog(
            dialog_id=DI2496_WHERES_THE_CROWN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
