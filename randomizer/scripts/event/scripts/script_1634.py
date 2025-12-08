# pylint: disable=C0301

"""E1634_FIREWORKS_HOUSE_LEFT_GIRL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1143_BEAN_VALLEY_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
