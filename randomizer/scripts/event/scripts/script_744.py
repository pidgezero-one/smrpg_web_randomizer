# pylint: disable=C0301

"""E0744_NIMBUS_LAND_LIBERATED_CASTLE_INNER_CELLAR_REWARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED, ["EVENT_744_run_dialog_54"]
        ),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        SetBit(NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED),
        Return(),
        RunDialog(
            dialog_id=DI0061_NIMBUS_NPC_AFTER_GIVING_YOU_FINAL_CELLAR_PRIZE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_744_run_dialog_54",
        ),
        Return(),
    ]
)
