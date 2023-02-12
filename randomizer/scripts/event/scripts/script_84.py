# E0084_THREE_MUSTY_FEARS_BONES_DIALOG

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_84_run_dialog_1"]),
        RunDialog(
            dialog_id=DI1105_MUSTY_FEARS_EXPLANATION,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED),
        RunDialog(
            dialog_id=DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_84_run_dialog_1",
        ),
        Return(),
    ]
)
