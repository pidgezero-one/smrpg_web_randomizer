# pylint: disable=C0301

"""E3722_NIMBUS_CASTLE_LEFT_CELLAR_WOMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3666_BEANSTALK_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
