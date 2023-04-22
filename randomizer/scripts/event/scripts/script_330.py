# pylint: disable=C0301

"""E0330_CHANCELLOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0568_CHANCELLOR,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASCopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
                ASFaceEast7C(),
            ],
        ),
        Return(),
    ]
)
