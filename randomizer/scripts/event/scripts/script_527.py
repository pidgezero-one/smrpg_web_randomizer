# pylint: disable=C0301

"""E0527_ROSE_TOWN_SHOP_RED_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0869_SHOP_TYPING_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
