# pylint: disable=C0301

"""E3131_MOLEVILLE_TOAD_IN_MINES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7043_0),
        RunDialog(
            dialog_id=DI1663_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ClearBit(TEMP_7043_0),
        Return(),
    ]
)
