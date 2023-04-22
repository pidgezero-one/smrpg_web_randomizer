# pylint: disable=C0301

"""E0631_MARRYMORE_KITCHEN_CHEF_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2062_APPRENTICE_CHEF,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
