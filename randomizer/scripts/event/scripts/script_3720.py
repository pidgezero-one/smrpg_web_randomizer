# pylint: disable=C0301

"""E3720_NIMBUS_CASTLE_OUTER_CELLAR_BLUE_GIFT_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BLUE_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_3720_run_dialog_10"]),
        SetBit(BLUE_CELLAR_GUARD_ITEM_GRANTED),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
        RunDialog(
            dialog_id=DI3667_CELLAR_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3720_run_dialog_10"),
        Return(),
    ]
)
